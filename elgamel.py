import random

# Parameters
p = 29  # A large prime number
g = 7   # Generator
private_key = 5  # Bob's private key
public_key = pow(g, private_key, p)

# Display public and private information
print(f"Public Key: {public_key}")
print(f"Prime (p): {p}, Generator (g): {g}, Private Key (Hidden): {private_key}")

# Message to encrypt
message = 10  # Example plaintext message

# Random session key (k)
k = random.randint(1, p - 2)

# Encryption
c1 = pow(g, k, p)
c2 = (message * pow(public_key, k, p)) % p

# Ciphertext
ciphertext = (c1, c2)
print(f"Ciphertext: {ciphertext}")

# Decryption
shared_secret = pow(c1, private_key, p)
decrypted_message = (c2 * pow(shared_secret, -1, p)) % p
print(f"Decrypted Message: {decrypted_message}")
