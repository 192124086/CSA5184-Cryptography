import numpy as np

def hill_encrypt(key_matrix, plaintext):
    # Remove spaces and convert plaintext to uppercase
    plaintext = ''.join(plaintext.split()).upper()
    key_matrix = np.array(key_matrix)
    
    n = len(key_matrix)
    ciphertext = ''
    
    # Add padding if necessary
    if len(plaintext) % n != 0:
        plaintext += 'X' * (n - len(plaintext) % n)
    
    for i in range(0, len(plaintext), n):
        block = [ord(char) - ord('A') for char in plaintext[i:i+n]]
        block = np.array(block)
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join([chr(num + ord('A')) for num in encrypted_block])
    
    return ciphertext

def hill_decrypt(key_matrix, ciphertext):
    key_matrix = np.array(key_matrix)
    inverse_key_matrix = np.linalg.inv(key_matrix)
    
    n = len(key_matrix)
    plaintext = ''
    
    for i in range(0, len(ciphertext), n):
        block = [ord(char) - ord('A') for char in ciphertext[i:i+n]]
        block = np.array(block)
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        plaintext += ''.join([chr(num + ord('A')) for num in decrypted_block])
    
    return plaintext

# Provided key matrix
key_matrix = [[9, 4], [5, 7]]

# Original plaintext
plaintext = "meet me at the usual place at ten rather than eight oclock"

# Encrypt the plaintext
ciphertext = hill_encrypt(key_matrix, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_plaintext = hill_decrypt(key_matrix, ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
