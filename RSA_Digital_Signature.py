from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate RSA keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Original message
original_message = b"Trust is built using PKI!"

# Signing the original message
signature = private_key.sign(
    original_message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Modified message (tampered)
tampered_message = b"Trust is broken without PKI!"

# Verifying the signature with the tampered message
try:
    public_key.verify(
        signature,
        tampered_message,  # This is different from the original message
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verified successfully!")
except Exception as e:
    print("Verification failed:", e)
