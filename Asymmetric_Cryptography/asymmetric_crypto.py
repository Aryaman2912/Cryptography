from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class AliceGenerate():
    """
    This class generates the public and private keys of Alice.
    """
    def generate_private_key(self):
        # Generation of Alice's private key
        # private_key is an object
        privatekey = rsa.generate_private_key(

            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # The below function converts the private_key object into a byte string
        pemprivatekey = privatekey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
        )
        return pemprivatekey

    def generate_public_key(self):
        # Generate Alice's public key
        # public_key is an object
        publickey = privatekey.public_key()

        # The below code converts the public_key object to into a byte string
        pempublickey = publickey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pempublickey

    def __init__(self, publickey, privatekey):
        self.private_key = __privatekey
        self.publickey = publickey


class BobGenerate():
    """
    This class generates the public and private keys of Bob.
    """
    def generate_private_key(self):
        # Generation of Bob's private key
        # private_key is an object
        privatekey = rsa.generate_private_key(

            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # The below function converts the private_key object into a byte string
        pemprivatekey = privatekey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
        )
        return pemprivatekey,privatekey

    def generate_public_key(self,privatekey):
        # Generate Bob's public key
        # public_key is an object
        publickey = privatekey.public_key()

        # The below code converts the public_key object to into a byte string
        pempublickey = publickey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pempublickey

