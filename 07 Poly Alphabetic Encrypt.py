def generate_key(plaintext, key):
    key = list(key)
    if len(key) < len(plaintext):
        key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    return ''.join(key)
def encrypt_vigenere(plaintext, key):
    ciphertext = []
    key = generate_key(plaintext, key).upper()
    for i in range(len(plaintext)):
        if plaintext[i].isalpha(): 
            shift = ord(key[i]) - ord('A')
            if plaintext[i].isupper():
                enc_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
            else:
                enc_char = chr(((ord(plaintext[i]) - ord('a') + shift) % 26) + ord('a'))
            ciphertext.append(enc_char)
        else:
            ciphertext.append(plaintext[i])

    return ''.join(ciphertext)

plaintext = input("Enter The Plain Text: ")
key_encrypt = input("Enter The Key in Capital Letter: ")
ciphertext = encrypt_vigenere(plaintext, key_encrypt)
print("Plaintext:", plaintext)
print("Key:", key_encrypt)
print("Ciphertext:", ciphertext)