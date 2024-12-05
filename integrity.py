import hashlib

# Compute SHA-256 hash
data = b"Important Transaction Records"
sha256_hash = hashlib.sha256(data).hexdigest()

print(f"SHA-256 Hash: {sha256_hash}")
