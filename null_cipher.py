def encode_null_cipher(message, cover_text):
    """Encodes a message using a null cipher technique by modifying the first letters of the cover text."""
    words = cover_text.split()
    
    # Extend cover text to match the message length
    if len(words) < len(message):
        words = (words * (len(message) // len(words) + 1))[:len(message)]

    encoded = ""
    for i, word in enumerate(words):
        if i < len(message):
            encoded += message[i] + word[1:] + " "
        else:
            encoded += word + " "
    return encoded.strip()

def decode_null_cipher(encoded_text, original_cover_text):
    """Decodes a message hidden using a null cipher."""
    encoded_words = encoded_text.split()
    cover_words = original_cover_text.split()
    
    # Extend cover text if needed for decoding
    if len(cover_words) < len(encoded_words):
        cover_words = (cover_words * (len(encoded_words) // len(cover_words) + 1))[:len(encoded_words)]

    decoded_message = ""
    for encoded_word, cover_word in zip(encoded_words, cover_words):
        if encoded_word[0] != cover_word[0]:  # Detect modified first letter
            decoded_message += encoded_word[0]
    return decoded_message

# Main Program
def main():
    print("Null Cipher Encoder/Decoder")
    print("1. Encode a message")
    print("2. Decode a message")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        # Encoding
        message = input("Enter the message to encode: ").strip().upper()
        cover_text = input("Enter the cover text: ").strip()
        encoded_text = encode_null_cipher(message, cover_text)
        print("\nEncoded Text:")
        print(encoded_text)
    elif choice == "2":
        # Decoding
        encoded_text = input("Enter the encoded text: ").strip()
        original_cover_text = input("Enter the original cover text: ").strip()
        decoded_message = decode_null_cipher(encoded_text, original_cover_text)
        print("\nDecoded Message:")
        print(decoded_message)
    else:
        print("Invalid choice. Please choose 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()
11