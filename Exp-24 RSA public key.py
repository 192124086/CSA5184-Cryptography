def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    if b == 0:
        x, y = 1, 0
        return a, x, y

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        print("Inverse does not exist.")
        return -1

    result = (x % m + m) % m
    return result

def main():
    e = 31
    n = 3599

    for p in range(2, n + 1):
        if n % p == 0:
            q = n // p
            break

    phi_n = (p - 1) * (q - 1)

    d = mod_inverse(e, phi_n)

    print("Private key d:", d)

if __name__ == "__main__":
    main()
