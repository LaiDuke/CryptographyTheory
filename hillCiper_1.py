import numpy as np
from egcd import egcd
from numpy.linalg import inv

originalMessage = np.matrix([13,14,12])
encryptKey = np.matrix([[3,10,20],[20,19,17], [23,78,17]])





encryptedMessage = np.dot(originalMessage, encryptKey) % 27
print(encryptedMessage)


def matrix_mod_inv(matrix, modulus):

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)

    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)

    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )

    return matrix_modulus_inv



# decryptionKey = inv(np.matrix(encryptKey))
# print(decryptionKey)
decryptionKey = matrix_mod_inv(np.matrix(encryptKey), 27)
print(decryptionKey)

# Our decrypted matrix is
decryptedMessage = np.dot(originalMessage, decryptionKey) % 27
print(decryptedMessage)