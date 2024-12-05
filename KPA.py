def find_caesar_key(plaintext, ciphertext):
    return (ord(ciphertext[0]) - ord(plaintext[0])) % 26

plaintext = "HELLO"
ciphertext = "KHOOR"  # Caesar cipher with a shift of 3
key = find_caesar_key(plaintext, ciphertext)
print("Detected Key:", key)
