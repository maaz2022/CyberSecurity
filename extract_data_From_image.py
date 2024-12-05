from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = img.getdata()
    binary_message = ''

    for pixel in pixels:
        binary_message += str(pixel[2] & 1)

    # Convert binary to text
    secret_message = ''.join(chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8))
    print(f"Extracted Message: {secret_message}")

# Usage
decode_image("example.jpg")
