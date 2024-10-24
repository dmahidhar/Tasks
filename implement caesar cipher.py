Edef caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a given text using the Caesar Cipher algorithm.
    
    Parameters:
    - text (str): The message to encrypt or decrypt.
    - shift (int): The shift value.
    - mode (str): 'encrypt' to encrypt, 'decrypt' to decrypt.
    
    Returns:
    - str: The resulting encrypted or decrypted text.
    """
    result = ""
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Determine ASCII offset based on uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Perform the shift within the alphabet range
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted_char
        else:
            # Keep non-alphabetic characters as is
            result += char

    return result

def get_shift_value():
    """
    Gets a valid shift value from the user.
    
    Returns:
    - int: A validated shift value.
    """
    while True:
        try:
            shift = int(input("Enter the shift value (can be positive or negative): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("Advanced Caesar Cipher")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt or (Q)uit? ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice not in ('E', 'D'):
            print("Invalid choice. Please choose 'E' for encryption, 'D' for decryption, or 'Q' to quit.")
            continue

        text = input("Enter your message: ")
        shift = get_shift_value()
        mode = 'encrypt' if choice == 'E' else 'decrypt'

        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
