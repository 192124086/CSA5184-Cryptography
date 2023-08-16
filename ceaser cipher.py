def caesar_cipher(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)
message = input("Enter Message:")
shift = int(input("Enter Shift Key:"))
encrypted_message = caesar_cipher(message, shift)
print("Encrypted message:",encrypted_message) 
