# The following program contains an implementation of the vigenère cipher.
# It works only on alphabetical strings

# Input the plaintext and key
plaintext = input("Enter the string to be encrypted(alphabetical): ")
key = input("Enter the key to be used(alphabetical): ")

# variable to track the index of key being used
i = 0

# list to store ciphertext
ciphertext = []

# For each character, check if the character is uppercase or lowercase and then encrypt it accordingly
for l in plaintext:

	# character is lowercase
	if l.islower():
		res = chr((ord(l) + ord(key[i].lower()) - 194) % 26 + ord('a')).lower()
	
	# character is uppercase
	elif l.isupper():
		res = chr((ord(l) + ord(key[i].upper()) - 130) % 26 + ord('A')).upper()
	
	# character is not part of the alphabet
	else:
		print("Input should only contain uppercase and lowercase letters!")
		break

	ciphertext.append(res)

	# Ensure that i stays within key length
	i = (i + 1) % len(key)

# Convert the list to string and print the ciphertext
print("The encrypted string is: ")
print(''.join(ciphertext))