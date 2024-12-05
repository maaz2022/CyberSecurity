from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate DSA private key
private_key = dsa.generate_private_key(key_size=2048)

# Sign a message
message = b"Secure Update File"
signature = private_key.sign(message, hashes.SHA256())

# Verify the signature
public_key = private_key.public_key()
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature verification successful!")
except:
    print("Signature verification failed.")
