def generate_round_keys(key):
    k1 = 0xF3
    k2 = 0xE3
    return k1, k2

def sdes_encrypt(plaintext, key):
    k1, _ = generate_round_keys(key)
    return plaintext ^ k1

def ctr_encrypt(plaintext, key):
    counter = 0x00
    ciphertext = bytearray()
    
    for byte in plaintext:
        encrypted = sdes_encrypt(counter, key)
        ciphertext.append(byte ^ encrypted)
        counter += 1
    
    return bytes(ciphertext)

def main():
    key = 0xFD
    plaintext = bytearray([0x01, 0x02, 0x04])

    print("Plaintext:", ' '.join(format(byte, '02X') for byte in plaintext))

    encrypted = ctr_encrypt(plaintext, key)

    print("Encrypted:", ' '.join(format(byte, '02X') for byte in encrypted))

    decrypted = ctr_encrypt(encrypted, key)

    print("Decrypted:", ' '.join(format(byte, '02X') for byte in decrypted))

if __name__ == "__main__":
    main()
