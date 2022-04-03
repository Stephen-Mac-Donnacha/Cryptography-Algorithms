from collections import OrderedDict


# Method that breaks the plaintext into pairs of 2 letters also called digraphs
def break_plaintxt(plaintxt):
    digraph_string = ""
    c = 0
    # Iterates over the length of the plaintext
    while c < len(plaintxt):
        # If we get to the end of the string and it's odd
        # we append an 'X' to the end of it
        if c == len(plaintxt) - 1:
            digraph_string += plaintxt[c]
            digraph_string += 'X'
        # If 2 concurrent characters are unique, add them to digraph_string
        # otherwise we append the letter and then we append an 'X' to it before
        # we add it to digraph_string
        elif plaintxt[c] != plaintxt[c + 1]:
            digraph_string += plaintxt[c]
            digraph_string += plaintxt[c + 1]
        else:
            # c-=1 to take a step back after we pad out 2 recurring characters
            # with an 'X'
            digraph_string += plaintxt[c]
            digraph_string += 'X'
            c -= 1
        c += 2

    print("The plain text in digraphs is:", digraph_string)
    return digraph_string


# Method to replace the letters 'J' and 'K' with 'I' and 'C'
# respectively in accordance with the assignment description
def clean_txt(s):
    s = s.replace('J', 'I')
    s = s.replace('K', 'C')
    return s


# Method that generates the matrix to be used by the cipher algorithm
def generate_matrix(key):
    alpha = "ABCDEFGHILMNOPQRSTUVWXYZ "
    key = clean_txt(key)
    total_alpha = key + alpha
    final = list(OrderedDict.fromkeys(total_alpha))

    # Create the encryption matrix here
    matrix = []
    for i in range(5):
        m = []
        for j in range(5):
            m.append(final[i * 5 + j])
        matrix.append(m)

    return matrix


# Method to locate the index of a character in the cipher matrix
# needed to perform encryption
def index_locator(char, cipher_key_matrix):
    char_index = []

    # Swap J/K for I/C
    if char == 'J':
        char = 'I'

    if char == 'K':
        char = 'C'

    for i, j in enumerate(cipher_key_matrix):
        for k, l in enumerate(j):

            if char == l:
                char_index.append(i)  # add 1st dimension of 5X5 matrix => i.e., indexOfChar = [i]
                char_index.append(k)  # add 2nd dimension of 5X5 matrix => i.e., indexOfChar = [i,k]
                return char_index


# Method to encrypt the plaintext
def encrypt_plaintext(plaintxt, key):
    ciphertxt = []

    # Generate key matrix
    key_matrix = generate_matrix(key)

    i = 0
    while i < len(plaintxt) - 1:
        n1 = index_locator(plaintxt[i], key_matrix)
        n2 = index_locator(plaintxt[i + 1], key_matrix)

        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]

            i2 = (n2[0] + 1) % 5
            j2 = n2[1]
            ciphertxt.append(key_matrix[i1][j1])
            ciphertxt.append(key_matrix[i2][j2])
        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] + 1) % 5

            i2 = n2[0]
            j2 = (n2[1] + 1) % 5
            ciphertxt.append(key_matrix[i1][j1])
            ciphertxt.append(key_matrix[i2][j2])
            # exchange columns of both value
        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            ciphertxt.append(key_matrix[i1][j2])
            ciphertxt.append(key_matrix[i2][j1])
        i += 2
    print("The cipher text is: ", ciphertxt)
    return ciphertxt


# Method to decrypt the ciphertext
def decrypt_ciphertxt(plaintxt, key):
    ciphertxt = []

    # Generate key matrix
    key_matrix = generate_matrix(key)

    i = 0
    while i < len(plaintxt) - 1:
        n1 = index_locator(plaintxt[i], key_matrix)
        n2 = index_locator(plaintxt[i + 1], key_matrix)

        if n1[1] == n2[1]:
            i1 = (n1[0] + 4) % 5
            j1 = n1[1]

            i2 = (n2[0] + 4) % 5
            j2 = n2[1]
            ciphertxt.append(key_matrix[i1][j1])
            ciphertxt.append(key_matrix[i2][j2])
        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] + 4) % 5

            i2 = n2[0]
            j2 = (n2[1] + 4) % 5
            ciphertxt.append(key_matrix[i1][j1])
            ciphertxt.append(key_matrix[i2][j2])
            # exchange columns of both value
        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            ciphertxt.append(key_matrix[i1][j2])
            ciphertxt.append(key_matrix[i2][j1])
        i += 2
    return ciphertxt


# Main method
def viginere_cipher():
    # Getting user inputs Key (to make the 5x5 char matrix) and Plain Text (Message that is to be encripted)
    key = input("Enter key: ").replace(" ", "").upper()
    plaintxt = input("Plain Text: ").replace(" ", "").upper()

    # Break plaintext into digraphs
    convertedPlainText = break_plaintxt(plaintxt)

    cipherText = "".join(encrypt_plaintext(convertedPlainText, key))
    # Strip , and space from the ciphertext
    cipherText.strip(',')
    cipherText.strip(' ')
    # Print the cipher text
    print(cipherText)

    decipheredtxt = decrypt_ciphertxt(cipherText, key)
    print(decipheredtxt)

