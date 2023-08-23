def mod_exp(base, exp, modulus):
    result = 1
    base %= modulus
    while exp > 0:
        if exp & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exp >>= 1
    return result

def encrypt(character, e, n):
    return mod_exp(character, e, n)

def main():
    p = 9973  # Example prime numbers (should be much larger in practice)
    q = 9857
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    message = input("Enter the message (all uppercase letters without spaces): ").strip()

    print("Encrypted message:", end=" ")
    for char in message:
        character = ord(char) - ord('A')  # Convert character to number (A=0, B=1, ..., Z=25)
        encrypted_char = encrypt(character, e, n)
        print(encrypted_char, end=" ")

    print()

if __name__ == "__main__":
    main()
