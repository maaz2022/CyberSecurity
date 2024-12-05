import pyotp

# Generate a base32 secret key
totp = pyotp.TOTP(pyotp.random_base32())

# Generate and verify OTP
print(f"One-Time Password: {totp.now()}")
otp = input("Enter OTP: ")
if totp.verify(otp):
    print("Authentication successful.")
else:
    print("Authentication failed.")
