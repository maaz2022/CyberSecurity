from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key(key_size=16):
    """
    Generate a random key for AES encryption.
    :param key_size: Length of the key in bytes (default is 16 for AES-128).
    :return: A randomly generated key.
    """
    if key_size not in [16, 24, 32]:
        raise ValueError("Invalid key size. Key size must be 16, 24, or 32 bytes.")
    return get_random_bytes(key_size)

def encrypt_data(plaintext, key):
    """
    Encrypt plaintext using AES in ECB mode.
    :param plaintext: Data to be encrypted (must be bytes).
    :param key: Key for encryption (must match the AES mode).
    :return: Encrypted ciphertext.
    """
    block_size = AES.block_size  # AES block size is 16 bytes
    padded_plaintext = pad(plaintext, block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(padded_plaintext)

def decrypt_data(ciphertext, key):
    """
    Decrypt ciphertext using AES in ECB mode.
    :param ciphertext: Data to be decrypted (must be bytes).
    :param key: Key for decryption (must match the AES mode).
    :return: Decrypted plaintext.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, AES.block_size)

def main():
    """
    Main function to handle user choices for encryption or decryption.
    """
    try:
        print("Welcome to AES Encryption/Decryption!")
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            # Encryption process
            key = generate_key()
            print(f"Generated Key (Hex): {key.hex()}")
            
            plaintext = input("Enter the text you want to encrypt: ").strip().encode()
            ciphertext = encrypt_data(plaintext, key)
            print(f"Ciphertext (Hex): {ciphertext.hex()}")
            print("Save this key and ciphertext for decryption!")

        elif choice == "2":
            # Decryption process
            key_hex = input("Enter the key (Hex format): ").strip()
            ciphertext_hex = input("Enter the ciphertext (Hex format): ").strip()

            key = bytes.fromhex(key_hex)
            ciphertext = bytes.fromhex(ciphertext_hex)
            
            decrypted_text = decrypt_data(ciphertext, key).decode()
            print(f"Decrypted Text: {decrypted_text}")

        else:
            print("Invalid choice. Please enter 1 for encryption or 2 for decryption.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
