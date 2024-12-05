private_key = [2, 3, 7, 14, 30]  # Super-increasing sequence
modulus = 61
multiplier = 17

# Generate public key
public_key = [(multiplier * x) % modulus for x in private_key]

# Message to encrypt (binary representation)
message = [1, 0, 1, 1, 0]

# Encryption
ciphertext = sum([m * k for m, k in zip(message, public_key)])
print("Ciphertext:", ciphertext)

# Decryption
mod_inverse = pow(multiplier, -1, modulus)
c = (ciphertext * mod_inverse) % modulus

# Recover original message using private key
recovered_message = []
for x in reversed(private_key):
    if c >= x:
        recovered_message.append(1)
        c -= x
    else:
        recovered_message.append(0)

recovered_message.reverse()
print("Decrypted Message:", recovered_message)
