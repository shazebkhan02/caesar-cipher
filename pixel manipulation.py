from PIL import Image
import numpy as np

def encrypt_image(image_path, shift_value):
    # Load the image
    image = Image.open(image_path)
    # Convert the image to a NumPy array
    image_array = np.array(image)
    
    # Encrypt the image by adding the shift value to each pixel
    encrypted_array = (image_array + shift_value) % 256
    
    # Convert the array back to an image
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    
    # Save the encrypted image
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, shift_value):
    # Load the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    # Convert the image to a NumPy array
    encrypted_array = np.array(encrypted_image)
    
    # Decrypt the image by subtracting the shift value from each pixel
    decrypted_array = (encrypted_array - shift_value) % 256
    
    # Convert the array back to an image
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    
    # Save the decrypted image
    decrypted_image.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'.")

def main():
    # Get user input
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter the path to the image: ")
    shift_value = int(input("Enter the shift value (integer): "))
    
    if mode == 'encrypt':
        encrypt_image(image_path, shift_value)
    elif mode == 'decrypt':
        decrypt_image(image_path, shift_value)
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
