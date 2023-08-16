import string
# Create a mapping between the plaintext alphabet and the ciphertext alphabet.
plaintext_alphabet = string.ascii_lowercase
ciphertext_alphabet = "abcdefghijklmnopqrstuvwxyz"[::-1]
mapping = dict(zip(plaintext_alphabet, ciphertext_alphabet))
# Encrypt a message.
message = input("Enter Message:")
encrypted_message = ""
for letter in message:
    if letter in mapping:
        encrypted_message += mapping[letter]
    else:
        encrypted_message += letter
print("Encrypted message:",encrypted_message)
# Decrypt a message.
decrypted_message = ""
for letter in encrypted_message:
    if letter in mapping:
        decrypted_message += mapping[letter]
    else:
        decrypted_message += letter
print("Decrypted message:",decrypted_message)
