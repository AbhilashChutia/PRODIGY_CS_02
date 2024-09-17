from PIL import Image
import numpy as np

# Encryption and decryption key (you can change this to any value)
ENCRYPTION_KEY = 255  # Simple XOR key

def encrypt_image(input_image_path, output_image_path):
    # Open the input image
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure image is in RGB mode
    
    # Convert image to NumPy array
    data = np.array(img)
    
    # Encrypt each pixel by applying XOR with the ENCRYPTION_KEY
    encrypted_data = np.bitwise_xor(data, ENCRYPTION_KEY)
    
    # Convert the encrypted data back to an image
    encrypted_img = Image.fromarray(encrypted_data.astype(np.uint8))
    
    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img = img.convert('RGB')
    
    # Convert image to NumPy array
    data = np.array(img)
    
    # Decrypt each pixel by applying XOR with the ENCRYPTION_KEY (reverses the encryption)
    decrypted_data = np.bitwise_xor(data, ENCRYPTION_KEY)
    
    # Convert the decrypted data back to an image
    decrypted_img = Image.fromarray(decrypted_data.astype(np.uint8))
    
    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

# Example usage:
if __name__ == "__main__":
    input_image = 'image.jpeg'   # Path to the input image
    encrypted_image = 'encrypted_image.jpg'  # Path to save the encrypted image
    decrypted_image = 'decrypted_image.jpg'  # Path to save the decrypted image
    
    # Encrypt the image
    encrypt_image(input_image, encrypted_image)
    
    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image)
