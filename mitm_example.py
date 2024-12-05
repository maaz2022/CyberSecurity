# mitm_example.py
import ssl
import socket
from cryptography.fernet import Fernet

class SecureConnection:
    def __init__(self):
        # Generate encryption key
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

class Client:
    def __init__(self, secure_connection):
        self.secure = secure_connection
        
    def send_sensitive_data(self, data):
        # Encrypt data before sending
        encrypted_data = self.secure.cipher_suite.encrypt(data.encode())
        return encrypted_data

class Server:
    def __init__(self, secure_connection):
        self.secure = secure_connection
        
    def receive_data(self, encrypted_data):
        # Decrypt received data
        decrypted_data = self.secure.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()

class MITMAttacker:
    def intercept_unencrypted(self, data):
        print(f"[MITM Attack] Successfully intercepted unencrypted data: {data}")
        # Attacker could modify data here
        return data
    
    def attempt_intercept_encrypted(self, encrypted_data):
        print("[MITM Attack] Failed to read encrypted data:", encrypted_data)
        return encrypted_data

def demonstrate_mitm():
    # Scenario 1: Unsecured Communication
    print("\nScenario 1: Unsecured Communication")
    print("------------------------------------")
    sensitive_data = "username=john&password=secret123"
    attacker = MITMAttacker()
    
    # Simulate unsecured data transmission
    intercepted_data = attacker.intercept_unencrypted(sensitive_data)
    print("This shows how easily unencrypted data can be intercepted!")

    # Scenario 2: Secured Communication
    print("\nScenario 2: Secured Communication")
    print("------------------------------------")
    # Setup secure connection
    secure_conn = SecureConnection()
    client = Client(secure_conn)
    server = Server(secure_conn)
    
    # Simulate secure data transmission
    sensitive_data = "username=john&password=secret123"
    encrypted_data = client.send_sensitive_data(sensitive_data)
    
    # Attacker tries to intercept
    attacker.attempt_intercept_encrypted(encrypted_data)
    
    # Server successfully decrypts
    received_data = server.receive_data(encrypted_data)
    print(f"Server successfully decrypted data: {received_data}")

if __name__ == "__main__":
    demonstrate_mitm()