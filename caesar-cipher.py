def caesar_cipher(text, shift, mode='encrypt'):
    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    # Adjust the shift for decryption mode
    if mode == 'decrypt':
        shift = -shift
    
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is a letter
        if char.upper() in alphabet:
            # Find the index of the character in the alphabet
            index = alphabet.index(char.upper())
            
            # Calculate the new index based on the shift
            new_index = (index + shift) % 26
            
            # Get the shifted character
            new_char = alphabet[new_index]
            
            # Maintain the original case of the character
            result += new_char.lower() if char.islower() else new_char
        else:
            # Append non-alphabet characters without changes
            result += char
    
    return result

def main():
    # Get user input for the message and shift value
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))
    
    # Choose mode
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    # Check mode and perform the corresponding action
    if mode in ['encrypt', 'decrypt']:
        output = caesar_cipher(message, shift, mode)
        print(f"Output ({mode}ed message): {output}")
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
