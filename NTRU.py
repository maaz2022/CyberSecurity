from sympy import mod_inverse

# Key generation
p, q = 7, 11
n = p * q  # Public key
private_key = (p, q)

# Message
message = 9
if message >= n:
    raise ValueError(f"Message must be less than n={n}")

# Encryption
ciphertext = (message ** 2) % n
print("Ciphertext:", ciphertext)

# Decryption
mp = pow(ciphertext, (p + 1) // 4, p)
mq = pow(ciphertext, (q + 1) // 4, q)

# Chinese Remainder Theorem
yp = mod_inverse(q, p)
yq = mod_inverse(p, q)

# Compute the possible plaintexts
solutions = [
    (mp * q * yq + mq * p * yp) % n,
    (mp * q * yq - mq * p * yp) % n,
    (-mp * q * yq + mq * p * yp) % n,
    (-mp * q * yq - mq * p * yp) % n,
]

# Ensure all solutions are positive modulo n
solutions = [sol % n for sol in solutions]
print("Possible plaintexts:", solutions)

# Identifying the correct solution
if message in solutions:
    correct_message = message
    print("Original Message:", correct_message)
else:
    print("Error: Original message not found in possible solutions.")
