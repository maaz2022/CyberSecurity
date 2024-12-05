def xor_decrypt(ciphertext, key):
    return ''.join(chr(ord(c) ^ key) for c in ciphertext)

ciphertext = xor_encrypt("HELLO", 123)  # Reuse previous example
decrypted = xor_decrypt(ciphertext, 123)
print("Decrypted Ciphertext:", decrypted)
