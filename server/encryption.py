import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256


key = PBKDF2HMAC(
    SHA256(),
    length=32,
    salt="".encode(),
    iterations=20000
).derive("techtalents".encode())

cipher = Fernet(base64.urlsafe_b64encode(key))

# Encryption
def encrypt(plaintext):
    encoded_pt = plaintext.encode()
    ciphertext = cipher.encrypt(encoded_pt)
    return ciphertext.decode()


# Decryption
def decrypt(ciphertext):
    print(f"{ciphertext = }")
    decrypted = cipher.decrypt(ciphertext.encode())
    print("decrypted =", list(decrypted))
    plaintext = decrypted.decode()
    print(f"{plaintext = }")
    return plaintext
