
from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Load image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Perform encryption
    encrypted_array = (img_array + key) % 256
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved at {output_path}")

def decrypt_image(input_path, output_path, key):
    # Load image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Perform decryption
    decrypted_array = (img_array - key) % 256
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved at {output_path}")

# Example usage
if __name__ == "__main__":
    key = 50  # Default encryption key
    encrypt_image("sample_image.jpg", "encrypted_image.png", key)
    decrypt_image("encrypted_image.png", "decrypted_image.jpg", key)
