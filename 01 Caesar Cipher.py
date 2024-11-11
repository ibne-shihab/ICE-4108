def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift letter within alphabet
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char  # Non-alphabetic characters remain the same
    return result

# Decrypt with Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)



# Get user input for plaintext and shift
text = input("Enter the plain text: ")
shift = int(input("Enter the shift key (1-25): "))

# Encrypt the text
encrypted_text = encrypt(text, shift)
print("Encrypted Text:", encrypted_text)

# Decrypt the text back using known shift
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)

