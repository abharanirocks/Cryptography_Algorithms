def generate_playfair_matrix(key):
    key = key.replace("j", "i")  # Replace 'j' with 'i'
    key = "".join(dict.fromkeys(key))  # Remove duplicate letters
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # Remove 'j' from the alphabet
    for char in key:
        alphabet = alphabet.replace(char, "")
    matrix = list(key) + list(alphabet)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def playfair_cipher_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    encrypted_text = ""
    i = 0
    while i < len(plain_text):
        char1, char2 = plain_text[i], plain_text[i + 1]
        row1, col1 = find_matrix_position(matrix, char1)
        row2, col2 = find_matrix_position(matrix, char2)
        if row1 == row2:  # Same row
            encrypted_text += matrix[row1][(col1 + 1) %
                                           5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += matrix[(row1 + 1) %
                                     5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Forming a rectangle
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        i += 2
    return encrypted_text


def playfair_cipher_decrypt(encrypted_text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    i = 0
    while i < len(encrypted_text):
        char1, char2 = encrypted_text[i], encrypted_text[i + 1]
        row1, col1 = find_matrix_position(matrix, char1)
        row2, col2 = find_matrix_position(matrix, char2)
        if row1 == row2:  # Same row
            decrypted_text += matrix[row1][(col1 - 1) %
                                           5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += matrix[(row1 - 1) %
                                     5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Forming a rectangle
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        i += 2
    return decrypted_text


def find_matrix_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


# Example usage:
plain_text = "ILoveYou".lower()
# plain_text = "I LoveYou".lower().strip()
key = "keyword"
encrypted_text = playfair_cipher_encrypt(plain_text, key)
print("Encrypted:", encrypted_text)
decrypted_text = playfair_cipher_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
