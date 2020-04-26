import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def add_padding(string):
    """
    This function adds padding to a message i.e, if the message length is not an integral multiple of 16, trailing spaces
    are added to make it a multiple of 16.
    """
    space = ' '
    if (len(string) % 16) != 0:
        rem = len(string) % 16 
        string += space*(16-rem)
        
    return string

def remove_padding(string):
    """
    This function removes any extra padding that was added.
    """ 
    return " ".join(string.split())
        
def encrypt(plaintext:str):
    """
    This function contains code to encrypt a message.
    """
    backend = default_backend()
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return key,ct,iv

def decrypt(key,ct,iv):
    """
    This function contains code to decrypt a message.
    """
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ct) + decryptor.finalize()
    return decrypted_message.decode()

#User input
sent_message = input("Enter a string to be encrypted: ")
#Add padding if required
padded_string = add_padding(sent_message)
#Convert string to byte string which will be used during encryption
byte_string = padded_string.encode()
#Encrypt the message
key,ct,iv = encrypt(byte_string)
print(f'key - {key} \n ct - {ct} \n iv - {iv}')
#Decrypt the message
decrypted_message = decrypt(key,ct,iv)
#Remove extra padding
recieved_message = remove_padding(decrypted_message)
print(f"The decrypted message is '{recieved_message}'")
