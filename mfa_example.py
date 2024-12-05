import random
import time
import qrcode
import pyotp
import smtplib
import logging
from email.mime.text import MIMEText
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime, timedelta
import sys

# Configure logging to monitor system activity
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class User:
    """
    Represents a user in the MFA system.
    - `username`: The username of the user.
    - `password_hash`: A hashed password (use real hashing in production).
    - `email`: The user's email address for communication.
    - `phone`: The user's phone number for SMS or backup communication.
    - `totp_secret`: Secret for TOTP generation.
    - `backup_codes`: List of one-time backup codes for account recovery.
    """
    username: str
    password_hash: str  # In production, hash passwords securely
    email: str
    phone: str
    totp_secret: Optional[str] = None
    backup_codes: List[str] = None

class MFASystem:
    """
    Implements the MFA system with TOTP, email verification, and backup codes.
    Handles user registration, login, and session management.
    """
    def __init__(self):
        # Store registered users
        self.users = {}
        # Active user sessions
        self.active_sessions = {}
        # Temporary storage for email verification codes
        self.email_codes = {}
        
    def register_user(self, username: str, password: str, email: str, phone: str) -> User:
        """
        Registers a new user and generates necessary MFA components (e.g., TOTP and backup codes).
        Returns the created `User` object.
        """
        # Create a new user object with dummy password hashing
        user = User(
            username=username,
            password_hash=password,  # Replace with a proper hash in production
            email=email,
            phone=phone,
            totp_secret=pyotp.random_base32(),  # Generate a TOTP secret key
            backup_codes=self._generate_backup_codes()  # Generate backup codes
        )
        # Add the user to the system
        self.users[username] = user
        logging.info(f"User {username} registered successfully")
        return user
    
    def _generate_backup_codes(self, count: int = 8) -> List[str]:
        """
        Generates a list of backup codes for account recovery.
        Backup codes are unique, single-use strings.
        """
        return [
            ''.join(random.choices('0123456789ABCDEF', k=8))
            for _ in range(count)
        ]
    
    def setup_totp(self, username: str) -> str:
        """
        Configures TOTP for the specified user and returns the provisioning URI.
        This URI can be used to set up TOTP on an authenticator app.
        """
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found")
        
        # Generate a provisioning URI for the user's authenticator app
        totp = pyotp.TOTP(user.totp_secret)
        provisioning_uri = totp.provisioning_uri(
            user.email,
            issuer_name="SecureApp MFA"
        )
        
        try:
            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=5
            )
            qr.add_data(provisioning_uri)
            qr.make(fit=True)
            
            # Create an image from the QR Code (optional)
            # qr.make_image(fill_color="black", back_color="white").save("qr_code.png")
            
            logging.info(f"TOTP setup completed for user {username}")
            return provisioning_uri
            
        except Exception as e:
            logging.error(f"Error generating QR code: {e}")
            return provisioning_uri  # Return URI even if QR generation fails
    
    def send_email_code(self, username: str) -> bool:
        """
        Sends a one-time code to the user's email for verification purposes.
        Returns `True` if successful.
        """
        user = self.users.get(username)
        if not user:
            return False
        
        # Generate a 6-digit code
        code = ''.join(random.choices('0123456789', k=6))
        # Save the code with an expiration time
        self.email_codes[username] = {
            'code': code,
            'expires': datetime.now() + timedelta(minutes=5)  # Code valid for 5 minutes
        }
        
        try:
            # Log the code instead of sending a real email (for demo purposes)
            logging.info(f"Email code for {username}: {code}")
            return True
        except Exception as e:
            logging.error(f"Failed to send email code: {e}")
            return False
    
    def verify_first_factor(self, username: str, password: str) -> bool:
        """
        Verifies the first factor (username and password).
        Returns `True` if successful.
        """
        user = self.users.get(username)
        if not user:
            return False
        
        # Compare the provided password (hashing omitted for simplicity)
        return user.password_hash == password
    
    def verify_totp(self, username: str, totp_code: str) -> bool:
        """
        Verifies the TOTP code provided by the user.
        Returns `True` if the code matches the user's secret.
        """
        user = self.users.get(username)
        if not user or not user.totp_secret:
            return False
        
        totp = pyotp.TOTP(user.totp_secret)
        return totp.verify(totp_code)
    
    def verify_email_code(self, username: str, code: str) -> bool:
        """
        Verifies the email verification code provided by the user.
        Returns `True` if the code matches and hasn't expired.
        """
        if username not in self.email_codes:
            return False
        
        code_data = self.email_codes[username]
        if datetime.now() > code_data['expires']:
            del self.email_codes[username]
            return False
        
        is_valid = code_data['code'] == code
        if is_valid:
            del self.email_codes[username]
        return is_valid
    
    def verify_backup_code(self, username: str, code: str) -> bool:
        """
        Verifies a backup code provided by the user.
        Consumes the code upon successful verification.
        """
        user = self.users.get(username)
        if not user or not user.backup_codes:
            return False
        
        if code in user.backup_codes:
            user.backup_codes.remove(code)  # Remove used code
            return True
        return False
    
    def login(self, username: str, password: str, second_factor_type: str, second_factor_code: str) -> bool:
        """
        Handles the full login process, including:
        1. Verifying the password (first factor).
        2. Verifying the second factor (TOTP, email code, or backup code).
        Returns `True` if login succeeds.
        """
        # Step 1: Verify username and password
        if not self.verify_first_factor(username, password):
            logging.warning(f"First factor failed for user {username}")
            return False
        
        # Step 2: Verify the second factor
        second_factor_verified = False
        if second_factor_type == 'totp':
            second_factor_verified = self.verify_totp(username, second_factor_code)
        elif second_factor_type == 'email':
            second_factor_verified = self.verify_email_code(username, second_factor_code)
        elif second_factor_type == 'backup':
            second_factor_verified = self.verify_backup_code(username, second_factor_code)
        
        # Step 3: Handle login success
        if second_factor_verified:
            # Generate a session token (use secure methods in production)
            session_token = random.randbytes(32).hex()
            self.active_sessions[session_token] = {
                'username': username,
                'expires': datetime.now() + timedelta(hours=24)  # Token valid for 24 hours
            }
            logging.info(f"Successful login for user {username}")
            return session_token
        
        logging.warning(f"Second factor failed for user {username}")
        return False

def demonstrate_mfa():
    """
    Demonstrates the functionality of the MFA system with various scenarios.
    """
    try:
        mfa_system = MFASystem()
        
        # Register a new user
        print("\n1. Registering new user...")
        user = mfa_system.register_user(
            "john_doe",
            "secure_password123",
            "john@example.com",
            "+1234567890"
        )
        
        # Setup TOTP for the user
        print("\n2. Setting up TOTP...")
        try:
            totp_uri = mfa_system.setup_totp("john_doe")
            print(f"TOTP URI: {totp_uri}")
        except Exception as e:
            print(f"Error setting up TOTP: {e}")
            
        # Send an email verification code
        print("\n3. Sending email verification code...")
        mfa_system.send_email_code("john_doe")
        
        # Simulate login attempts
        print("\n4. Simulating login attempts...")
        
        # Failed password attempt
        print("\nAttempt 1: Wrong password")
        result = mfa_system.login("john_doe", "wrong_password", "totp", "000000")
        print(f"Login success: {bool(result)}")
        
        # Failed TOTP attempt
        print("\nAttempt 2: Correct password, wrong TOTP")
        result = mfa_system.login("john_doe", "secure_password123", "totp", "000000")
        print(f"Login success: {bool(result)}")
        
        # Successful login using a backup code
        print("\nAttempt 3: Correct password, valid backup code")
        backup_code = user.backup_codes[0]
        result = mfa_system.login("john_doe", "secure_password123", "backup", backup_code)
        print(f"Login success: {bool(result)}")
        
        # Show remaining backup codes
        print("\nRemaining backup codes:", user.backup_codes)
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        logging.error(f"Demonstration failed: {e}")

if __name__ == "__main__":
    # Run the demonstration
    demonstrate_mfa()

