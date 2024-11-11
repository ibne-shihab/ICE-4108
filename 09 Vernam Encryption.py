def vernam_encrypt(plaintext, key):
    ciphertext = []
    # Ensure key length matches the length of the plaintext
    if len(plaintext) != len(key):
        raise ValueError("Key length must be equal to the plaintext length.")
    for i in range(len(plaintext)):
        # XOR between the binary representation of plaintext and key characters
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i]))
        ciphertext.append(encrypted_char)

    return ''.join(ciphertext)
plaintext = input("Enter The Plain Text: ")
key_encrypt = input("Enter The Key in Capital Letter: ")
ciphertext = vernam_encrypt(plaintext, key_encrypt)
print("Plaintext:", plaintext)
print("Key:",key_encrypt)
print("Ciphertext:", ''.join(format(ord(c), '02x') for c in ciphertext))