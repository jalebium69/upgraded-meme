import math

def create_matrix(text, key, fill_char='X'):
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    padded_text = text.ljust(num_rows * num_cols, fill_char)
    
    matrix = []
    for i in range(num_rows):
        row = list(padded_text[i * num_cols:(i + 1) * num_cols])
        matrix.append(row)
    
    return matrix

def encrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    matrix = create_matrix(text, key)
    
    cipher_text = ''
    for col in key_order:
        for row in matrix:
            cipher_text += row[col]
    
    return cipher_text

def decrypt(cipher_text, key):
    num_cols = len(key)
    num_rows = math.ceil(len(cipher_text) / num_cols)
    
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    decipher_matrix = [[''] * num_cols for _ in range(num_rows)]
    
    col_length = len(cipher_text) // num_cols
    extra_chars = len(cipher_text) % num_cols
    
    index = 0
    for col in key_order:
        current_col_length = col_length + 1 if col < extra_chars else col_length
        for row in range(current_col_length):
            decipher_matrix[row][col] = cipher_text[index]
            index += 1
    
    plain_text = ''.join([''.join(row) for row in decipher_matrix]).rstrip('X')
    
    return plain_text

# Example usage:
plaintext = "MODESOFOPERATION"
key = "3142"

# Encrypt the plaintext
print(f'Plaintext: {plaintext}')
print(f'Key: {key}')
encrypted_text = encrypt(plaintext.replace(" ", ""), key)
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = decrypt(encrypted_text, key)
print(f"Decrypted: {decrypted_text}")
