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


# def my_algorithm_encrypt(plain, key):
#     print("My Algorithm ")
#     cipher = ""
#     for i in range(key):
#         cipher = caesar_encrypt(plain, i)
#         cipher = revert_text(cipher)
#         cipher = caesar_encrypt(cipher, key-i)
#     print("\tThe cipher text is : ", cipher)
#     return cipher
#
#
# def my_algorithm_decrypt(cipher, key):
#     print("My Algorithm ")
#     plain = ""
#     for i in range(key):
#         plain = caesar_decrypt(cipher, key-i)
#         plain = revert_text(plain)
#         plain = caesar_decrypt(plain, i)
#     print("\tThe plain text is : ", plain)
#     return plain


def caesar_encrypt(plain):
    print("\nCaesar Encryption Algorithm")
    print("\tPlain Text : " + plain)
    s = 3
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


def shift_encrypt(plain, s):
    print("\nshift_encrypt Encryption Algorithm")
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


def shift_decrypt(cipher, s):
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


def multi_encrypt(plain, s):
    print("\nmulti_encrypt Encryption Algorithm")
    print("\tPlain Text : " + plain)
    print("\tMulti Key : " + str(s))
    cipher = ""
    for i in range(len(plain)):
        char = plain[i]
        if char.isupper():
            cipher += chr((ord(char) - 65) * s % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) - 97) * s % 26 + 97)
        else:
            cipher += char
    print("\tThe cipher text is : ", cipher)
    return cipher


def affine_encrypt(plain, k1, k2):
    print("\naffine_encrypt Encryption Algorithm")
    print("\tPlain Text : " + plain)
    print("\tPair of Key : (" + str(k1) + ", " + str(k2) + ")")
    cipher = ""
    for i in range(len(plain)):
        char = plain[i]
        if char.isupper():
            cipher += chr(((ord(char) - 65) * k1 + k2) % 26 + 65)
        elif char.islower():
            cipher += chr(((ord(char) - 97) * k1 + k2) % 26 + 97)
        else:
            cipher += char
    print("\tThe cipher text is : ", cipher)
    return cipher


def auto_key_encrypt(plain, s):
    print("\nauto_key_encrypt Encryption Algorithm")
    print("\tPlain Text : " + plain)
    print("\tK1 : " + str(s))
    cipher = ""
    for i in range(len(plain)):
        char = plain[i]
        if char.isupper():
            cipher += chr((ord(char) + s - 65) % 26 + 65)
            if i != 0:
                s = ord(char) - 65
        elif char.islower():
            cipher += chr((ord(char) + s - 97) % 26 + 97)
            if i != 0:
                s = ord(char) - 97
        else:
            cipher += char
    print("\tThe cipher text is : ", cipher)
    return cipher


def vigen_encrypt(plain, s):
    print("\nvigen_encrypt Encryption Algorithm")
    print("\tPlain Text : " + plain)
    print("\tKey : " + s)
    cipher = ""
    for i in range(len(plain)):
        char = plain[i]
        if i >= len(s):
            index = i % len(s)
        else:
            index = i
        if char.isupper():
            cipher += chr((ord(char) - 65 + ord(s[index].upper()) - 65) % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) - 97 + ord(s[index].lower()) - 97) % 26 + 97)
        else:
            cipher += char
    print("\tThe cipher text is : ", cipher)
    return cipher


def main():
    affine_encrypt("Luonglinh", 3, 2)
    # plain_text = "iloveyou"
    # vigen_encrypt(plain_text, "nonooonaodnasdaso")
    auto_key_encrypt("Attack is today", 12)


if __name__ == '__main__':
    main()
