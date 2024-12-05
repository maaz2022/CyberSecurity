from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

try:
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Export private key in PEM format
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Export public key in PEM format
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save private key to a file
    with open('private_key.pem', 'wb') as private_file:
        private_file.write(pem_private_key)
        print("Private key saved to 'private_key.pem'.")

    # Save public key to a file
    with open('public_key.pem', 'wb') as public_file:
        public_file.write(pem_public_key)
        print("Public key saved to 'public_key.pem'.")

    # Verify file contents
    with open('private_key.pem', 'rb') as private_file:
        print("Private Key File Contents:")
        print(private_file.read().decode('utf-8'))

    with open('public_key.pem', 'rb') as public_file:
        print("Public Key File Contents:")
        print(public_file.read().decode('utf-8'))

except Exception as e:
    print(f"An error occurred: {e}")
