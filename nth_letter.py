import random
from PIL import Image

def add_noise(image_path, output_path, noise_level=1):
    img = Image.open(image_path)
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            r = min(255, max(0, r + random.randint(-noise_level, noise_level)))
            pixels[i, j] = (r, g, b)
    img.save(output_path)
    print("Noise added to image!")

# Usage
add_noise("output_image.jpg", "noisy_image.png", noise_level=10)
