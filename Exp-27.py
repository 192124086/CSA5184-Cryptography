def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus

    return result

def main():
    n = 12345678901
    e = 65537
    d = 123456789

    message = "HELLO"
    message_length = len(message)

    print("Original Message:", message)
    
    print("Encrypted Message:", end=" ")
    for char in message:
        encrypted = mod_pow(ord(char) - ord('A'), e, n)
        print(encrypted, end=" ")
    print()

    print("Decrypted Message:", end=" ")
    for char in message:
        encrypted = mod_pow(ord(char) - ord('A'), e, n)
        decrypted = (mod_pow(encrypted, d, n) + ord('A')) % 26  # Ensure it's in the range of 'A' to 'Z'
        print(chr(decrypted + ord('A')), end="")
    print()

if __name__ == "__main__":
    main()
