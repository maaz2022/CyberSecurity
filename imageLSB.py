from PIL import Image

def hide_message(image_path, output_path, message):
    img = Image.open(image_path).convert("RGB")  # Ensure compatibility
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'  # Add null terminator
    pixels = img.load()

    idx = 0
    for i in range(img.width):
        for j in range(img.height):
            if idx < len(binary_message):
                r, g, b = pixels[i, j]
                r = (r & ~1) | int(binary_message[idx])  # Modify LSB of red channel
                pixels[i, j] = (r, g, b)
                idx += 1

    img.save(output_path, "PNG")  # Use lossless format
    print("Message hidden successfully!")



# Usage
hide_message('input_image.jpg', 'output_image.jpg', 'HELLO')
