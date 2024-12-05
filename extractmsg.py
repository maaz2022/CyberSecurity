from PIL import Image

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    binary_message = ""

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            binary_message += str(r & 1)  # Extract LSB of red channel

    # Convert binary to string
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == "00000000":  # Stop at null terminator
            break
        message += chr(int(byte, 2))

    return message


# Usage
hidden_message = extract_message('output_image.jpg')
print("Extracted Message:", hidden_message)
