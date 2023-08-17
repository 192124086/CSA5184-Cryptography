class PlayfairCipher:
    def __init__(self, key):
        self.key = key.upper().replace("J", "I")
        self.matrix = self.generate_matrix()

    def generate_matrix(self):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_chars = list(self.key)
        matrix = []
        for char in key_chars:
            if char not in matrix:
                matrix.append(char)
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_char_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == char:
                    return row, col

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
        if len(plaintext) % 2 != 0:
            plaintext += "X"

        encrypted_text = ""
        for i in range(0, len(plaintext), 2):
            char1 = plaintext[i]
            char2 = plaintext[i + 1]
            row1, col1 = self.find_char_position(char1)
            row2, col2 = self.find_char_position(char2)

            if row1 == row2:
                encrypted_text += self.matrix[row1][(col1 + 1) % 5]
                encrypted_text += self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += self.matrix[(row1 + 1) % 5][col1]
                encrypted_text += self.matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += self.matrix[row1][col2]
                encrypted_text += self.matrix[row2][col1]

        return encrypted_text

# Example usage
keyword = "KEYWORD"
playfair_cipher = PlayfairCipher(keyword)

plaintext = input("Enter Encrypt message:")
encrypted_text = playfair_cipher.encrypt(plaintext)
print("Encrypted:", encrypted_text)
