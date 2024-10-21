def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    text_as_int = [ord(i) for i in text.upper()]

    for i in range(len(text_as_int)):
        if mode == 'encrypt':
            value = (text_as_int[i] + key_as_int[i % key_length]) % 26
        elif mode == 'decrypt':
            value = (text_as_int[i] - key_as_int[i % key_length]) % 26
        
        result.append(chr(value + 65))
    
    return ''.join(result)

# Example usage:
plaintext = "JESHER"
key = "NAME"

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
# Encrypt the plaintext
encrypted_text = vigenere_cipher(plaintext, key, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
