from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# RSA Key Generation
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Encrypt a message
message = b"Secure financial transaction"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Generate hash for integrity
hash_obj = hashes.Hash(hashes.SHA256())
hash_obj.update(message)
digest = hash_obj.finalize()

print(f"Ciphertext: {ciphertext}")
print(f"Message Hash: {digest.hex()}")

