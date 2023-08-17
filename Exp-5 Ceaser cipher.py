import string
def gcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

def generate_key(a, b):
    
    if gcd(a, 26) != 1:
        return None
    return a, b

def encrypt(plaintext, key):
    
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():
            if letter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            index = ord(letter) - base
            a, b = key
            index = (a * index + b) % 26
            ciphertext += chr(base + index)
        else:
            ciphertext += letter
    return ciphertext

a = 5
b = 7
plaintext = input("Enter plaintext:")
key = generate_key(a, b)
if key is None:
    print('Invalid key')
else:
    ciphertext = encrypt(plaintext, key)
    print('Ciphertext:', ciphertext)
