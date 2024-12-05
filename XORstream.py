def xor_encrypt(plaintext, key):
    return ''.join(chr(ord(c) ^ key) for c in plaintext)

def xor_decrypt(ciphertext, key):
    return ''.join(chr(ord(c) ^ key) for c in ciphertext)

# Example usage
plaintext = "HELLO"
key = 123  # Example XOR key

# Encrypt the plaintext
ciphertext = xor_encrypt(plaintext, key)
print("Encrypted Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted = xor_decrypt(ciphertext, key)
print("Decrypted Ciphertext:", decrypted)
