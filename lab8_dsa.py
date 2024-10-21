import hashlib
import random

# Helper function: modular inverse using the extended Euclidean algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Parameters for DSA (These values are usually very large primes)
# For simplicity, we're using small primes
p = 23  # prime number
q = 11  # prime divisor of p-1
g = 2   # generator

# Key Generation
def generate_keys():
    # Private key x (randomly chosen from {1, ..., q-1})
    x = random.randint(1, q - 1)
    # Public key y
    y = pow(g, x, p)
    return x, y

# Signature Generation
def sign(message, x):
    # Hash the message using SHA-1 (or any hash function)
    hash_value = int(hashlib.sha1(message.encode()).hexdigest(), 16)
    while True:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = mod_inverse(k, q)
        s = (k_inv * (hash_value + x * r)) % q
        if s == 0:
            continue
        return (r, s)

# Signature Verification
def verify(message, r, s, y):
    if not (0 < r < q and 0 < s < q):
        return False
    hash_value = int(hashlib.sha1(message.encode()).hexdigest(), 16)
    w = mod_inverse(s, q)
    u1 = (hash_value * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q
    return v == r

# Example usage
x, y = generate_keys()  # Generate private (x) and public (y) keys
message = "Test message"
r, s = sign(message, x)  # Sign the message
print("Signature:", (r, s))
is_valid = verify(message, r, s, y)  # Verify the signature
print("Signature valid:", is_valid)
