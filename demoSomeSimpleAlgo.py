def revert_text(text):
    print("\nDrawBack")
    print("\tPlain Text : " + text)
    result = ""
    i = len(text) - 1
    while i >= 0:
        result = result + text[i]
        i = i - 1
    print("\tThe result text is : ", result)
    return result


def caesar_encrypt(plain, s):
    print("\nCaesar Encryption Algorithm")
    print("\tPlain Text : " + plain)
    print("\tShift pattern : " + str(s))
    cipher = ""
    for i in range(len(plain)):
        char = plain[i]
        if char.isupper():
            cipher += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) + s - 97) % 26 + 97)
        else:
            cipher += char
    print("\tThe cipher text is : ", cipher)
    return cipher


def caesar_decrypt(cipher, s):
    print("\nCaesar Decryption Algorithm")
    print("\tPlain Text : " + cipher)
    print("\tShift pattern : " + str(s))
    plain = ""
    for i in range(len(cipher)):
        char = cipher[i]
        if char.isupper():
            plain += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            plain += chr((ord(char) - s - 97) % 26 + 97)
        else:
            plain += char
    print("\tThe cipher text is : ", plain)
    return plain


def main():
    plain_text = "Mother Fucker"
    caesar_encrypt(plain_text, 1)
    # revert_text(revert_text(plain_text))
    # caesar_decrypt(caesar_encrypt(plain_text, s), s)
    # my_algorithm_decrypt(my_algorithm_encrypt(plain_text, s), s)


def my_algorithm_encrypt(plain, key):
    print("My Algorithm ")
    cipher = ""
    for i in range(key):
        cipher = caesar_encrypt(plain, i)
        cipher = revert_text(cipher)
        cipher = caesar_encrypt(cipher, key-i)
    print("\tThe cipher text is : ", cipher)
    return cipher


def my_algorithm_decrypt(cipher, key):
    print("My Algorithm ")
    plain = ""
    for i in range(key):
        plain = caesar_decrypt(cipher, key-i)
        plain = revert_text(plain)
        plain = caesar_decrypt(plain, i)
    print("\tThe plain text is : ", plain)
    return plain


if __name__ == '__main__':
    main()
