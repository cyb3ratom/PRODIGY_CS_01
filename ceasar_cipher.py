# Caesar Cipher Encryption and Decryption

def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                # Shift letter forward
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                # Shift letter backward
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            # Leave non-letter characters unchanged
            result += char

    return result

# Get user input
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))
mode = input("Choose mode (encrypt/decrypt): ").lower()

# Call the function and display result
output = caesar_cipher(message, shift, mode)
print(f"\nResult: {output}")