def create_playfair_matrix(key):
    key = key.replace("J", "I").replace(" ", "").upper()
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    
    for char in key_set:
        matrix.append(char)
        
    for char in alphabet:
        if char not in key_set:
            matrix.append(char)
            
    playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return playfair_matrix

def find_coordinates(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(matrix, message):
    message = message.replace("J", "I").replace(" ", "").upper()
    encrypted = ""
    i = 0
    
    while i < len(message):
        char1 = message[i]
        char2 = message[i+1] if i+1 < len(message) and message[i+1] != char1 else "X"
        
        row1, col1 = find_coordinates(matrix, char1)
        row2, col2 = find_coordinates(matrix, char2)
        
        if row1 == row2:
            encrypted += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted += matrix[row1][col2] + matrix[row2][col1]
        
        i += 2
    
    return encrypted

key = "MFH IJKUNOPQZVWXYELARGDSTBC"
message = "MUSTSEEYOUOVERCADOGANWESTCOMINGATONCE"
matrix = create_playfair_matrix(key)
encrypted = playfair_encrypt(matrix, message)
print(encrypted)
