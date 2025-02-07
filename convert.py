import cv2


def generate_patt(image_path, output_patt_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize to 16x16 as required by ARToolKit
    image = cv2.resize(image, (16, 16), interpolation=cv2.INTER_AREA)

    # Normalize pixel values to the range 0.0 - 1.0
    normalized_image = image / 255.0

    # Write the .patt file
    with open(output_patt_path, "w") as f:
        f.write("16 16\n")  # Header: size of pattern
        for row in normalized_image:
            f.write(" ".join(f"{pixel:.6f}" for pixel in row) + "\n")

    print(f"Pattern file saved to {output_patt_path}")


# Example usage
generate_patt("2212.png", "2212.patt")
