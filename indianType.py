from Crypto.Cipher import AES
from Crypto.Util.Padding import *
key = input()
encryption_suite = AES.new(key.encode(), AES.MODE_ECB)
file = open("Home.mp3", "rb").read()
cipher_text = encryption_suite.encrypt(pad(file, AES.block_size))
result = open("Mp3Result.mp3", "wb")
result.write(cipher_text)
file = open("Mp3Result.mp3", "rb").read()
plain = unpad(encryption_suite.decrypt(file), AES.block_size)
result = open("Mp3Result.mp3", "wb")
result.write(plain)

