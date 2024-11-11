import numpy as np
def create_key_matrix(key):
    
    key_matrix = []
    k = 0
    for i in range(3):
        row = [ord(key[k + j]) % 65 for j in range(3)]
        key_matrix.append(row)
        k += 3
    return np.array(key_matrix)

def text_to_vector(text):
    """Convert text to vector form."""
    return np.array([[ord(char) % 65] for char in text])

def vector_to_text(vector):
    """Convert vector back to text."""
    return ''.join(chr(int(num) + 65) for num in vector.flatten())
def encrypt_message(plaintext, key):
    """Encrypt the plaintext message using the Hill cipher."""
    key_matrix = create_key_matrix(key)
    message_vector = text_to_vector(plaintext)
    cipher_vector = np.dot(key_matrix, message_vector) % 26
    return vector_to_text(cipher_vector)
def mod_inverse(a, m):
    """Compute modular inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1
def decrypt_message(ciphertext, key):
    """Decrypt the ciphertext message using the Hill cipher."""
    key_matrix = create_key_matrix(key)
    
    # Compute determinant and its modular inverse
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26
    determinant_inv = mod_inverse(determinant, 26)
    
    if determinant_inv == -1:
        raise ValueError("The key matrix is not invertible. Choose a different key.")
    
    # Compute adjugate matrix and modular inverse of the key matrix
    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)).astype(int) % 26
    key_matrix_inv = (determinant_inv * adjugate_matrix) % 26

    # Decrypt the ciphertext
    cipher_vector = text_to_vector(ciphertext)
    decrypted_vector = np.dot(key_matrix_inv, cipher_vector) % 26
    return vector_to_text(decrypted_vector)
# Fixed Key
key = input("Enter The Key: ")

# Input and Execution Flow
plaintext = input("Enter the plaintext (3 characters): ").upper()

if len(plaintext) != 3:
    print("Plaintext must be exactly 3 characters long.")
else:
    # Encryption
    ciphertext = encrypt_message(plaintext, key)
    
    # Decryption
    try:
        decrypted_text = decrypt_message(ciphertext, key)
        
        # Display Results
        print(f"Plaintext: {plaintext}")
        print(f"Key: {key}")
        print(f"Ciphertext: {ciphertext}")
        print(f"Decrypted Text: {decrypted_text}")

    except ValueError as e:
        print(e)
