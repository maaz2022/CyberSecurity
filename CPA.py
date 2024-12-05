def xor_encrypt(plaintext, key):
    return ''.join(chr(ord(c) ^ key) for c in plaintext)

chosen_plaintext = "HELLO"
key = 123  # Secret key
ciphertext = xor_encrypt(chosen_plaintext, key)
print("Ciphertext for chosen plaintext:", ciphertext)
