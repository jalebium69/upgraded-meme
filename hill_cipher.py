# Python3 code to implement Hill Cipher

# Initialize matrices
keyMatrix = [[0] * 3 for _ in range(3)]
messageVector = [[0] for _ in range(3)]
cipherMatrix = [[0] for _ in range(3)]
inverseKeyMatrix = [[0] * 3 for _ in range(3)]

# Function to generate the key matrix from the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to calculate the determinant of a 2x2 matrix
def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Function to calculate the determinant of a 3x3 matrix
def determinant(matrix):
    return (matrix[0][0] * determinant_2x2([[matrix[1][1], matrix[1][2]],
                                             [matrix[2][1], matrix[2][2]]]) -
            matrix[0][1] * determinant_2x2([[matrix[1][0], matrix[1][2]],
                                             [matrix[2][0], matrix[2][2]]]) +
            matrix[0][2] * determinant_2x2([[matrix[1][0], matrix[1][1]],
                                             [matrix[2][0], matrix[2][1]]]))

# Function to find the adjugate of a 3x3 matrix
def adjugate(matrix):
    cofactors = []
    for r in range(3):
        cofactorRow = []
        for c in range(3):
            # Create the minor matrix by removing row r and column c
            minor = [[matrix[i][j] for j in range(3) if j != c] for i in range(3) if i != r]
            cofactorRow.append(((-1) ** (r + c)) * determinant_2x2(minor))
        cofactors.append(cofactorRow)
    
    # Transpose the cofactor matrix to get the adjugate
    adjugate_matrix = [[cofactors[j][i] for j in range(3)] for i in range(3)]
    return adjugate_matrix

# Function to find the modular inverse of a number modulo 26
def mod_inverse(value, modulus):
    value = value % modulus
    for i in range(1, modulus):
        if (value * i) % modulus == 1:
            return i
    return -1  # No modular inverse found

# Function to find the inverse of the key matrix modulo 26
def inverseKeyMatrixFunction():
    det = determinant(keyMatrix)
    det_inv = mod_inverse(det, 26)
    if det_inv == -1:
        raise ValueError("Matrix is not invertible")

    adj = adjugate(keyMatrix)
    for i in range(3):
        for j in range(3):
            inverseKeyMatrix[i][j] = (adj[i][j] * det_inv) % 26

# Function to encrypt the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j]
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

# Function to decrypt the message
def decrypt(cipherMatrix):
    decryptedMatrix = [[0] for _ in range(3)]
    for i in range(3):
        for j in range(1):
            decryptedMatrix[i][j] = 0
            for x in range(3):
                decryptedMatrix[i][j] += inverseKeyMatrix[i][x] * cipherMatrix[x][j]
            decryptedMatrix[i][j] = decryptedMatrix[i][j] % 26

    decryptedText = []
    for i in range(3):
        decryptedText.append(chr(decryptedMatrix[i][0] + 65))
    
    return "".join(decryptedText)

def HillCipher(message, key):
    getKeyMatrix(key)

    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    # Encrypt the message
    encrypt(messageVector)

    # Generate the encrypted text from the cipher matrix
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    print("Ciphertext: ", "".join(CipherText))

    # Calculate the inverse key matrix for decryption
    inverseKeyMatrixFunction()

    # Decrypt the message
    decryptedText = decrypt(cipherMatrix)
    print("Decrypted Text: ", decryptedText)

# Driver Code
def main():
    message = "DOG"
    key = "GYBNQKURP"
    print("Original Message: ", message)
    print(f'Key: {key}')
    HillCipher(message, key)

if __name__ == "__main__":
    main()
