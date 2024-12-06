#
# https://techexpert.tips/python/python-using-aes-encryption/#google_vignette
#
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Function to encrypt using AES in CBC mode
# @parameter data: The text to decrypt
# @parameter key: the key to decrypt the ciphertext
# @parameter iv: The initialization vector
def encrypt_AES_CBC(data, key, iv):
    padder = padding.PKCS7(128).padder()  
    padded_data = padder.update(data.encode('utf-8'))  
    padded_data += padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())  
    encryptor = cipher.encryptor()  
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()  
    return ciphertext

# Function to decrypt using AES in CBC mode
# @parameter ciphertext: The ciphertext to decrypt
# @parameter key: the key to decrypt the ciphertext
# @parameter iv: The initialization vector
def decrypt_AES_CBC(ciphertext, key, iv):
    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()  
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize() 

    unpadder = padding.PKCS7(128).unpadder()  
    unpadded_data = unpadder.update(decrypted_data)  
    unpadded_data += unpadder.finalize()
    return unpadded_data.decode('utf-8')  



