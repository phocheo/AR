import cv2
import numpy as np

def generate_patt(image_path, output_patt_path):
    # Load image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    # Compute inner square boundaries (80% of 512x512)
    inner_size = int(min(w, h) * 0.8)
    margin = (min(w, h) - inner_size) // 2

    # Crop to inner black square
    cropped = image[margin:margin+inner_size, margin:margin+inner_size]

    # Resize to 16x16 for ARToolKit
    resized = cv2.resize(cropped, (16, 16), interpolation=cv2.INTER_AREA)

    # Normalize pixel values (range 0.0 - 1.0)
    normalized_image = resized / 255.0

    # Write .patt file
    with open(output_patt_path, "w") as f:
        f.write("16 16\n")  # Header: pattern size
        for row in normalized_image:
            f.write(" ".join(f"{pixel:.6f}" for pixel in row) + "\n")
    
    print(f"Pattern file saved to {output_patt_path}")

# Example usage
generate_patt("2212.png", "2212.patt")
