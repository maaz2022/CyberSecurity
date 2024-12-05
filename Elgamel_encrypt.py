import random

p = 29  # A large prime number
g = 7   # Generator
private_key = 5  # Bob's private key
public_key = pow(g, private_key, p)

# Message
message = 10
k = random.randint(1, p-2)  # Random session key

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
