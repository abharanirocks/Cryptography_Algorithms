def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                # Encrypt uppercase letters
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) +
                                     ord('A'))
            else:
                # Encrypt lowercase letters
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) +
                                     ord('a'))
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text


def caesar_decipher(text, shift):
    # Decryption is just like encryption but with a negative shift
    return caesar_cipher(text, -shift)


# Input from the user
plaintext = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (an integer): "))

# Encrypt the input text
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = caesar_decipher(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
