# Simulated WEP encryption vulnerability
def wep_encrypt(plaintext, key):
    return ''.join(chr((ord(c) + ord(key[i % len(key)])) % 256) for i, c in enumerate(plaintext))

def wep_cryptanalysis(ciphertext, known_plaintext):
    # Reverse the WEP-like encryption by guessing the key
    return ''.join(chr((ord(c) - ord(k)) % 256) for c, k in zip(ciphertext, known_plaintext))

key = "KEY"
plaintext = "HELLO"
ciphertext = wep_encrypt(plaintext, key)

# Attacker uses known plaintext to deduce ciphertext relationship
decrypted_text = wep_cryptanalysis(ciphertext, plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text (attack result):", decrypted_text)
