from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def private_key_generate():
	"""
	This functions contains code to generate a private key.
	Returns an object.
	"""
	private_key = rsa.generate_private_key(
    	public_exponent=65537,
    	key_size=2048,
    	backend=default_backend()
	)
	return private_key

def private_key_serialize(private_key):
	"""
	This function contains code to convert the private_key object to a byte string.
	Returns a byte string.
	"""
	serialized_private_key = private_key.private_bytes(
    	encoding=serialization.Encoding.PEM,
    	format=serialization.PrivateFormat.PKCS8,
    	encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
	)
	return serialized_private_key

def public_key_generate(private_key):
	"""
	This function contains code to generate the public key using the private key object.
	Returns an object.
	"""
	public_key = private_key.public_key()
	return public_key

def public_key_serialize(public_key):
	"""
	This function contains code to convert the public key object to a byte string.
	Returns a byte string.
	"""
	serialized_public_key = public_key.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
	)
	return serialized_public_key

def digital_signature(private_key,message):
	"""
	This function contains code to generate the digital signature using the private key.
	Returns a byte string.
	"""
	signature = private_key.sign(
		message,
		padding.PSS(
			mgf=padding.MGF1(hashes.SHA256()),
			salt_length=padding.PSS.MAX_LENGTH
		),
		hashes.SHA256()
	)
	return signature

def verification(public_key,message,signature):
	"""
	This function contains code to verify the digital signature.
	Raises exception if signature is invalid.
	"""
	public_key.verify(
		signature,
		message,
		padding.PSS(
			mgf=padding.MGF1(hashes.SHA256()),
			salt_length=padding.PSS.MAX_LENGTH
			),
		hashes.SHA256()
	)

def encrypt(message,public_key):
	"""
	This function contains code to encrypt a message with the available public key.
	Returns a byte string.
	"""
	ciphertext = public_key.encrypt(
		message,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)
	return ciphertext

def decrypt(ciphertext,private_key):
	"""
	This function contains code to decrypt a message with the private key.
	Returns a byte string.
	"""
	plaintext = private_key.decrypt(
		ciphertext,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)
	return plaintext

def alice_generate_key():
	"""
	This function contains code to generate Alice's private and public keys.
	"""
	private_key = private_key_generate()
	alice_private_key = private_key_serialize(private_key)	
	public_key = public_key_generate(private_key)
	alice_public_key = public_key_serialize(public_key)

def bob_generate_key():
	"""
	This function contains code to generate Bob's private and public keys.
	"""
	private_key = private_key_generate()
	bob_private_key = private_key_serialize(private_key)
	public_key = public_key_generate(private_key)
	alice_public_key = public_key_serialize(public_key)
