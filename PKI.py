from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509 import CertificateBuilder, NameOID
from cryptography import x509  # Import the x509 module
from cryptography.hazmat.primitives import hashes
from datetime import datetime, timedelta

# Generate RSA keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Simulate a CA issuing a certificate
subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "example.com")])

certificate = CertificateBuilder().subject_name(subject)\
    .issuer_name(issuer)\
    .public_key(public_key)\
    .serial_number(1000)\
    .not_valid_before(datetime.utcnow())\
    .not_valid_after(datetime.utcnow() + timedelta(days=365))\
    .sign(private_key, hashes.SHA256())

# Serialize certificate
certificate_pem = certificate.public_bytes(serialization.Encoding.PEM)
print(certificate_pem.decode())
