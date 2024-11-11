def vernam_decrypt_hex(ciphertext_hex, key):
    decrypted_text = []
    # Ensure the key length matches the plaintext length
    if len(ciphertext_hex) // 2 != len(key):
        raise ValueError("Key length must be equal to the ciphertext character length divided by 2.")
    # Convert each pair of hex digits to its integer value
    ciphertext_bytes = [int(ciphertext_hex[i:i+2], 16) for i in range(0, len(ciphertext_hex), 2)]
    for i in range(len(ciphertext_bytes)):
        # XOR each byte of ciphertext with each corresponding character in key
        decrypted_char = chr(ciphertext_bytes[i] ^ ord(key[i]))
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

ciphertext_hex = input("Enter The Cipher Text: ")
key = input("Enter The Key in Capital Letter: ")

decrypted_text = vernam_decrypt_hex(ciphertext_hex, key)
print("Ciphertext (Hex):", ciphertext_hex)
print("Key:", key)
print("Decrypted Text:", decrypted_text)