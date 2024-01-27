'''Python program to implement symmetric encryption using python library'''

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"KLE BCA GADAG")
print(token)
d = f.decrypt(token)
print(d)


