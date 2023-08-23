def mod_exp(base, exp, modulus):
    result = 1
    base = base % modulus

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp = exp >> 1
        base = (base * base) % modulus
    return result

def main():
    prime = 23
    base = 5

    alice_private_key = 6
    bob_private_key = 15

    alice_public_key = mod_exp(base, alice_private_key, prime)
    bob_public_key = mod_exp(base, bob_private_key, prime)

    print("Alice's Public Key:", alice_public_key)
    print("Bob's Public Key:", bob_public_key)

    alice_shared_secret = mod_exp(bob_public_key, alice_private_key, prime)
    bob_shared_secret = mod_exp(alice_public_key, bob_private_key, prime)

    print("Alice's Shared Secret:", alice_shared_secret)
    print("Bob's Shared Secret:", bob_shared_secret)

if __name__ == "__main__":
    main()
