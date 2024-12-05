from cryptography.fernet import Fernet

def encrypt_message(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

# Usage
key = Fernet.generate_key()
message = "SECRET"
encrypted = encrypt_message(message, key)
decrypted = decrypt_message(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
