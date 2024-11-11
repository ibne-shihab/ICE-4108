def generate_key(plaintext, key):
    key = list(key)
    if len(key) < len(plaintext):
        key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    return ''.join(key)
def decrypt_vigenere(ciphertext, key):
    plaintext = []
    key = generate_key(ciphertext, key).upper()
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i]) - ord('A')
            if ciphertext[i].isupper():
                dec_char = chr(((ord(ciphertext[i]) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                dec_char = chr(((ord(ciphertext[i]) - ord('a') - shift + 26) % 26) + ord('a'))
            plaintext.append(dec_char)
        else:
            plaintext.append(ciphertext[i])
    return ''.join(plaintext)

ciphertext = input("Enter The Cipher Text: ")
key = input("Enter The Key in capital letter to decrypt: ")
decrypted_text = decrypt_vigenere(ciphertext, key)
print("Ciphertext:", ciphertext)
print("Key:", key)
print("Decrypted text:", decrypted_text)