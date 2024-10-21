import itertools

def generate_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' is usually omitted or combined with 'I'
    key += ''.join([c for c in alphabet if c not in key])
    
    matrix = [list(key[i:i + 5]) for i in range(0, len(key), 5)]
    return matrix

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    processed_text = []
    
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
        else:
            char2 = 'X'
        
        if char1 == char2:
            processed_text.append(char1 + 'X')
            i += 1
        else:
            processed_text.append(char1 + char2)
            i += 2
    
    if len(processed_text[-1]) == 1:
        processed_text[-1] += 'X'
    
    return processed_text

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == char:
                return i, j
    return None

def playfair_cipher(text, key, mode='encrypt'):
    matrix = generate_playfair_matrix(key)
    digraphs = preprocess_text(text)
    result = []
    
    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:
            if mode == 'encrypt':
                result.append(matrix[row1][(col1 + 1) % 5])
                result.append(matrix[row2][(col2 + 1) % 5])
            elif mode == 'decrypt':
                result.append(matrix[row1][(col1 - 1) % 5])
                result.append(matrix[row2][(col2 - 1) % 5])
        
        elif col1 == col2:
            if mode == 'encrypt':
                result.append(matrix[(row1 + 1) % 5][col1])
                result.append(matrix[(row2 + 1) % 5][col2])
            elif mode == 'decrypt':
                result.append(matrix[(row1 - 1) % 5][col1])
                result.append(matrix[(row2 - 1) % 5][col2])
        
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])
    
    return ''.join(result)

# Example usage:
plaintext = "ELEPHANT"
key = "ANIMAL"
print(f"Plaintext: {plaintext}")
print(f'Key: {key}')
# Encrypt the plaintext
encrypted_text = playfair_cipher(plaintext, key, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = playfair_cipher(encrypted_text, key, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
