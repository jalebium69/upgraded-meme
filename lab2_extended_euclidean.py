def extended_gcd(a, b):
    """ Return GCD of a and b, and coefficients (x, y) such that a*x + b*y = gcd(a, b) """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """ Return the modulo inverse of a under modulo m, or None if it doesn't exist """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    else:
        return x % m  # Ensure the result is positive

# Example usage
if __name__ == "__main__":
    a = int(input("Enter a: "))
    m = int(input("Enter m: "))
    inverse = mod_inverse(a, m)
    if inverse is None:
        print(f"The modulo inverse of {a} under modulo {m} does not exist.")
    else:
        print(f"The modulo inverse of {a} under modulo {m} is: {inverse}")
