def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def break_affine_cipher(ciphertext, most_frequent, second_most_frequent):
    p_B = ord(most_frequent) - ord('A')
    p_U = ord(second_most_frequent) - ord('A')

    C_B = ord(ciphertext[0]) - ord('A')
    C_U = ord(ciphertext[1]) - ord('A')

    for a in range(1, 26):
        if mod_inverse(a, 26) is not None:
            b = (C_B - (a * p_B)) % 26
            if (a * p_U + b) % 26 == C_U:
                return a, b

    return None, None

ciphertext = "BU..."  # Replace with the actual ciphertext
most_frequent = "B"
second_most_frequent = "U"

a, b = break_affine_cipher(ciphertext, most_frequent, second_most_frequent)

if a is not None:
    print(f"Key (a, b): ({a}, {b})")
else:
    print("Could not break the cipher with the given information.")
