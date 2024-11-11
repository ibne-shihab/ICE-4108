def generate_key_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x))).replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is combined with 'I'
    key_matrix = []

    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)

    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]
def format_plaintext(plaintext):
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    formatted_text = ""
    i = 0

    while i < len(plaintext):
        formatted_text += plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            formatted_text += 'X'
        elif i + 1 < len(plaintext):
            formatted_text += plaintext[i + 1]
            i += 1
        i += 1

    if len(formatted_text) % 2 != 0:
        formatted_text += 'X'
    
    return formatted_text
def find_position(char, key_matrix):
    """Find the position of a character in the key matrix."""
    for i, row in enumerate(key_matrix):
        if char in row:
            return i, row.index(char)
    return None

def encrypt_pair(pair, key_matrix):
    row1, col1 = find_position(pair[0], key_matrix)
    row2, col2 = find_position(pair[1], key_matrix)

    if row1 == row2:  # Same row: move right
        return key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column: move down
        return key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle swap
        return key_matrix[row1][col2] + key_matrix[row2][col1]
def encrypt_playfair(plaintext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = format_plaintext(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i + 2]
        ciphertext += encrypt_pair(pair, key_matrix)
    return ciphertext

# Example usage
plaintext = input("Enter The Plain Text: ")
key_encrypt = input("Enter The Key in Capital Letter: ")
ciphertext = encrypt_playfair(plaintext, key_encrypt)
print("Plaintext:", plaintext)
print("The Key  is:", key_encrypt)
print("Ciphertext:", ciphertext)
def decrypt_pair(pair, key_matrix):
    row1, col1 = find_position(pair[0], key_matrix)
    row2, col2 = find_position(pair[1], key_matrix)

    if row1 == row2:  # Same row: move left
        return key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column: move up
        return key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle swap
        return key_matrix[row1][col2] + key_matrix[row2][col1]
def decrypt_playfair(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i + 2]
        plaintext += decrypt_pair(pair, key_matrix)
    return plaintext
ciphertext = input("Enter the cipher text: ")
key_decrypt = input("Enter The Key in Capital Letter: ")
decrypted_text = decrypt_playfair(ciphertext, key_decrypt)
print("Decrypted Text:", decrypted_text)