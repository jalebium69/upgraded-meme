def pad(s, n):
    return s + b'\0' * (n - len(s) % n)

def gmul(a, b):
    p = 0
    for counter in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        a &= 0xFF
        if hi_bit_set:
            a ^= 0x1B
        b >>= 1
    return p

def mix_columns(s):
    cpy = s[:]
    g = [2, 3, 1, 1]
    s[0] = gmul(g[0], cpy[0]) ^ gmul(g[1], cpy[1]) ^ gmul(g[2], cpy[2]) ^ gmul(g[3], cpy[3])
    s[1] = gmul(g[3], cpy[0]) ^ gmul(g[0], cpy[1]) ^ gmul(g[1], cpy[2]) ^ gmul(g[2], cpy[3])
    s[2] = gmul(g[2], cpy[0]) ^ gmul(g[3], cpy[1]) ^ gmul(g[0], cpy[2]) ^ gmul(g[1], cpy[3])
    s[3] = gmul(g[1], cpy[0]) ^ gmul(g[2], cpy[1]) ^ gmul(g[3], cpy[2]) ^ gmul(g[0], cpy[3])
    return s

def mix_columns_inv(s):
    g = [14, 11, 13, 9]
    cpy = s[:]
    s[0] = gmul(g[0], cpy[0]) ^ gmul(g[1], cpy[1]) ^ gmul(g[2], cpy[2]) ^ gmul(g[3], cpy[3])
    s[1] = gmul(g[3], cpy[0]) ^ gmul(g[0], cpy[1]) ^ gmul(g[1], cpy[2]) ^ gmul(g[2], cpy[3])
    s[2] = gmul(g[2], cpy[0]) ^ gmul(g[3], cpy[1]) ^ gmul(g[0], cpy[2]) ^ gmul(g[1], cpy[3])
    s[3] = gmul(g[1], cpy[0]) ^ gmul(g[2], cpy[1]) ^ gmul(g[3], cpy[2]) ^ gmul(g[0], cpy[3])
    return s

def aes_encrypt_block(plain_text, key):
    state = list(plain_text)
    for _ in range(10):
        state = mix_columns(state)
    encrypted_text = bytes(state)
    print("State after 10 rounds of mix_columns:")
    print_matrix([[state[i * 4 + j] for j in range(4)] for i in range(4)])
    return encrypted_text

def aes_decrypt_block(cipher_text, key):
    state = list(cipher_text)
    for _ in range(10):
        state = mix_columns_inv(state)
    decrypted_text = bytes(state)
    print("State after 10 rounds of mix_columns_inv:")
    print_matrix([[state[i * 4 + j] for j in range(4)] for i in range(4)])
    return decrypted_text

def aes_decrypt(cipher_text, key):
    decrypted_blocks = []
    block_size = 16
    for i in range(0, len(cipher_text), block_size):
        block = cipher_text[i:i+block_size]
        decrypted_block = aes_decrypt_block(block, key)
        print("Decrypted block:", decrypted_block.hex())
        decrypted_blocks.append(decrypted_block)
    
    decrypted_text = b''.join(decrypted_blocks).rstrip(b'\0')
    return decrypted_text

def print_matrix(matrix):
    for row in matrix:
        print(row)

def bytes_to_string(bytes_data):
    return bytes_data.decode('utf-8')

def string_to_bytes(string_data):
    return string_data.encode('utf-8')

def get_user_input():
    plain_text = input("Enter the plaintext (characters): ")
    key = input("Enter the key (characters): ")
    plain_text = string_to_bytes(plain_text)
    key = string_to_bytes(key)
    plain_text_padded = pad(plain_text, 16)
    key_padded = pad(key, 16)
    plain_text_hex = plain_text_padded.hex()
    key_hex = key_padded.hex()
    plain_text = bytes.fromhex(plain_text_hex)
    key = bytes.fromhex(key_hex)
    encrypted_block = aes_encrypt_block(list(plain_text), list(key))
    print("Encrypted block (after mix_columns):", encrypted_block.hex())
    
    decrypted_text = aes_decrypt(encrypted_block, list(key))
    print("Decrypted text:", bytes_to_string(decrypted_text))

if __name__ == "__main__":
    get_user_input()
