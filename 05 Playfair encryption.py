def generate_key_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x))).replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    key_matrix = []
    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    # Create a 5x5 matrix
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
    # If there's an odd number of characters, add an 'X' to the end
    if len(formatted_text) % 2 != 0:
        formatted_text += 'X'
    
    return formatted_text


def find_position(char, key_matrix):
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

plaintext = input("Enter Your Plain Text: ")
key = input("Enter Your key in Capital Letter: ")
ciphertext = encrypt_playfair(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)