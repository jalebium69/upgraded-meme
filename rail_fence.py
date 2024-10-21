def rail_fence_encrypt(text, key):
    # Create a 2D list (rail) to represent the zigzag pattern
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    
    # To determine the direction (down/up) on the rails
    direction_down = False
    row, col = 0, 0
    
    for char in text:
        # Place the character in the rail
        rail[row][col] = char
        col += 1
        
        # Change direction if we are at the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        
        # Move up or down in the rail pattern
        row += 1 if direction_down else -1
    
    # Read the characters row by row to form the ciphertext
    encrypted_text = ''.join([''.join(row) for row in rail])
    return encrypted_text

def rail_fence_decrypt(ciphertext, key):
    # Create a 2D list (rail) to mark the positions of characters
    rail = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    
    # To determine the direction (down/up) on the rails
    direction_down = None
    row, col = 0, 0
    
    # First mark the positions where characters will go
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        # Place a marker in the rail
        rail[row][col] = '*'
        col += 1
        
        row += 1 if direction_down else -1
    
    # Fill the rail with ciphertext
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1
    
    # Now read the matrix in zigzag manner to decrypt
    decrypted_text = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        # Append the character to the decrypted text
        decrypted_text.append(rail[row][col])
        col += 1
        
        row += 1 if direction_down else -1
    
    return ''.join(decrypted_text)

# Example usage:
plaintext = "ALL THE BEST"
key = 2
print(f'Plaintext: {plaintext}')
print(f'key: {key}')
# Encrypt the plaintext
encrypted_text = rail_fence_encrypt(plaintext.replace(" ", ""), key)
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = rail_fence_decrypt(encrypted_text, key)
print(f"Decrypted: {decrypted_text}")
