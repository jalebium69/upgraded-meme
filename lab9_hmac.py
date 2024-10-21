def simple_hash(message):
    """
    Custom simple hash function:
    - Split message into 8-bit chunks.
    - Convert each 8-bit chunk to a decimal value.
    - Sum all the decimal values.
    - Return the sum modulo 256 as a single byte.
    
    :param message: Input message as a byte string.
    :return: A single byte representing the hash (mod 256 of the sum of bytes).
    """
    print(message)
    total_sum = sum(message)  # Sum all the bytes (each byte is 8 bits)
    return total_sum % 256  # Return the result modulo 256


def hmac_simple_hash(key, message):
    """
    HMAC algorithm using a custom simple hash function.
    
    :param key: The secret key (byte string).
    :param message: The message to authenticate (byte string).
    :return: The HMAC digest as a byte.
    """
    block_size = 64  # Block size (in bytes, 512 bits)

    # If the key is longer than the block size, hash it first
    if len(key) > block_size:
        key = bytes([simple_hash(key)])

    # Ensure the key is exactly block_size by padding with zeros
    key = key.ljust(block_size, b'\x00')

    # Create inner and outer padded keys (ipad and opad)
    o_key_pad = bytes([k ^ 0x5C for k in key])  # Outer pad XOR with 0x5C
    i_key_pad = bytes([k ^ 0x36 for k in key])  # Inner pad XOR with 0x36

    # Perform HMAC: H((K ^ opad) || H((K ^ ipad) || message))
    inner_hash = bytes([simple_hash(i_key_pad + message)])  # Hash inner padding + message
    hmac_result = bytes([simple_hash(o_key_pad + inner_hash)])  # Hash outer padding + inner hash

    return hmac_result


if __name__ == "__main__":
    # Example secret key and message
    key = b"my_secret_key"
    message = b"this is a message"

    # Compute HMAC
    hmac_result = hmac_simple_hash(key, message)

    # Print the HMAC result
    print(f"HMAC result (custom hash): {hmac_result.hex()}")
