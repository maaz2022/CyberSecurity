from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate keys
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

# Signing a document
document = b"Classified Government Report"
signature = private_key.sign(document, hashes.SHA256())

# Verifying the signature
try:
    public_key.verify(signature, document, hashes.SHA256())
    print("Document is authentic and untampered.")
except:
    print("Verification failed.")
