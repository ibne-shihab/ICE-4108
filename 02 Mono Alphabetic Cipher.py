def create_cipher_key():
    import string
    import random
    
    alphabet = string.ascii_lowercase
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    cipher_key = dict(zip(alphabet, shuffled))
    return cipher_key

def encrypt(plaintext, cipher_key):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            char_lower = char.lower()
            cipher_char = cipher_key[char_lower]
            if char.isupper():
                ciphertext += cipher_char.upper()
            else:
                ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, cipher_key):
    reverse_key = {v: k for k, v in cipher_key.items()}
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            char_lower = char.lower()
            plain_char = reverse_key[char_lower]
            if char.isupper():
                plaintext += plain_char.upper()
            else:
                plaintext += plain_char
        else:
            plaintext += char
    return plaintext

# Example usage
cipher_key = create_cipher_key()

# Take input from the user
plaintext = input("Enter the plaintext to encrypt: ")

ciphertext = encrypt(plaintext, cipher_key)
decrypted_text = decrypt(ciphertext, cipher_key)

print("Plaintext:", plaintext)
print("Cipher Key:", cipher_key)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
