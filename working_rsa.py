from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Original plaintext message
plaintext = b"Bank Account Details"
print(f"Original Plaintext: {plaintext.decode()}")

# Encrypting the message
encrypted_message = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Display the encrypted message in base64 for readability
encrypted_message_base64 = base64.b64encode(encrypted_message).decode('utf-8')
print(f"Encrypted Message (Base64): {encrypted_message_base64}")

# Decrypting the encrypted message
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Display the decrypted message
print(f"Decrypted Message: {decrypted_message.decode()}")
