class PolyalphabeticCipher:
    def __init__(self, key):
        self.key = key.upper().replace(" ", "")
        self.key_len = len(self.key)
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace(" ", "")
        encrypted_text = ""

        for i, char in enumerate(plaintext):
            if char.isalpha():
                key_char = self.key[i % self.key_len]
                shift = self.alphabet.index(key_char)
                encrypted_char = self.shift_char(char, shift)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char

        return encrypted_text

    def shift_char(self, char, shift):
        index = self.alphabet.index(char)
        shifted_index = (index + shift) % 26
        return self.alphabet[shifted_index]

    def decrypt(self, ciphertext):
        decrypted_text = ""

        for i, char in enumerate(ciphertext):
            if char.isalpha():
                key_char = self.key[i % self.key_len]
                shift = self.alphabet.index(key_char)
                decrypted_char = self.reverse_shift_char(char, shift)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        return decrypted_text

    def reverse_shift_char(self, char, shift):
        index = self.alphabet.index(char)
        reversed_index = (index - shift) % 26
        return self.alphabet[reversed_index]

# Example usage
keyword = "KEY"
polyalphabetic_cipher = PolyalphabeticCipher(keyword)

plaintext = input("Enter message:")
encrypted_text = polyalphabetic_cipher.encrypt(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = polyalphabetic_cipher.decrypt(encrypted_text)
print("Decrypted:", decrypted_text)
