import struct
from math import sin, floor

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    # Initialize variables
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Define per-round shift amounts
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

    # Define K table
    K = [floor(abs(sin(i + 1)) * 2**32) for i in range(64)]

    # Pre-processing: add a single 1 bit
    msg = bytearray(message.encode())
    msg.append(0x80)

    # Pre-processing: padding with zeros
    while len(msg) % 64 != 56:
        msg.append(0)

    # Append original length in bits mod 2^64 to message
    msg += struct.pack('<Q', len(message) * 8)

    # Process the message in 16-word blocks
    for chunk_start in range(0, len(msg), 64):
        chunk = msg[chunk_start:chunk_start + 64]
        
        # Break chunk into sixteen 32-bit words
        M = [struct.unpack('<I', chunk[i:i + 4])[0] for i in range(0, 64, 4)]

        # Initialize hash value for this chunk
        a, b, c, d = A, B, C, D

        # Main loop
        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + K[i] + M[g]) & 0xFFFFFFFF, s[i])) & 0xFFFFFFFF
            a = temp

        # Add this chunk's hash to result
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Produce the final hash as a 32-byte string
    return struct.pack('<IIII', A, B, C, D).hex()

# Example usage
input_string="Jesher Joshua"
print(f'Plain text: {input_string}')
print(f'MD5 Hash: {md5(input_string)}')
