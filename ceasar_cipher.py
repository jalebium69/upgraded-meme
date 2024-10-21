def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    # Normalize the shift to be within the range of 0-25
    shift = shift % 26
    
    # If mode is decrypt, reverse the shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Non-alphabetic characters are added unchanged
            result += char
    
    return result

# Example usage:
plaintext = "Jesher"
shift_value = 3

print(f'Plaintext: {plaintext}')
# Encrypt the plaintext
encrypted_text = caesar_cipher(plaintext, shift_value, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = caesar_cipher(encrypted_text, shift_value, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
