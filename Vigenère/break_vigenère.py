import numpy as np
import re
max_key_length = 20
letters = 'abcdefghijklmnopqrstuvwxyz'

letter_frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
					  0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
					  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
					  0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

# Function to get index of coincidence for a string
def get_IoC(string):
	
	n = len(string)
	freq_sum = 0.0
	for l in letters:
		freq_sum += (string.count(l)*(string.count(l) - 1))
	ioc = freq_sum / (n*(n-1))

	return ioc

# Function to get key length using index of coincidence
def get_key_length(ciphertext):
	
	# This list stores the IoC values for all lengths of key upto 20
	ioc_list = []

	# For each value of length of key, find the average index of coincidence for all the subsequences obtained from it
	for l in range(max_key_length):
		ioc = 0
		ioc_avg = 0
		n = len(ciphertext)
		for j in range(l):
			string = ''
			i = j
			while i < n:
				string += ciphertext[i]
				i += l
			ioc += get_IoC(string)
		if l:
			ioc_avg = ioc/l
		ioc_list.append(ioc_avg)


	# Find the two best fits for length of the key
	best_length = ioc_list.index(sorted(ioc_list)[-1])
	best_length_2 = ioc_list.index(sorted(ioc_list)[-2])

	# If the one of the best fits divides the other, choose the smaller one as the key might be repeated
	if best_length_2 and best_length % best_length_2 == 0:
		return best_length_2
	else:
		return best_length

# Function to perform frequency analysis on a string
# This function uses chi squared test to find the best possible shift for the string 
def freq_analysis(string):

	chi_squared_list = [0]*26

	for i in range(26):
		chi_squared = 0.0

		offset = [((ord(string[j])-97-i)%26)+97 for j in range(len(string))]
		v = [0]*26
		for l in offset:
			v[l - ord('a')] += 1
		for j in v:
			 j /= float(len(string))
		for j in range(26):
			chi_squared += (v[j] - letter_frequencies[j]**2)/float(letter_frequencies[j])
		# chi_squared_sum = ((np.array(v) - np.array(letter_frequencies)**2)/float(np.array(letter_frequencies)))

		chi_squared_list[i] = chi_squared
	shift = chi_squared_list.index(min(chi_squared_list))
	return chr(shift + 97)

# Function to get key using the key length
def get_key(ciphertext,key_length):
	key = ''
	n = len(ciphertext)
	for j in range(key_length):
		string = ''
		i = j
		while i < n:
			string += ciphertext[i]
			i += key_length
		key += freq_analysis(string)
	return key

# Function to decrypt the ciphertext using the key
def decrypt(ciphertext,key):
	plaintext = ''
	i = 0
	for l in ciphertext:
		res = chr((ord(l) - ord(key[i].lower()) + 26) % 26 + ord('a')).lower()

		plaintext += res

		# Ensure that i stays within key length
		i = (i + 1) % len(key)
	return plaintext

# Function to remove any non alphabetic characters and convert string to lowercase
def process_string(ciphertext):
	regex = re.compile('[^a-zA-Z]')
	ciphertext = regex.sub('',ciphertext).lower()
	return ciphertext

# Main function
def main():

	ciphertext = input("Enter the ciphertext(only lowercase alphabets):\n")
	ciphertext = process_string(ciphertext)
	key_length = get_key_length(ciphertext)
	key = get_key(ciphertext,key_length)
	print(f'The most probable key is {key}')
	plaintext = decrypt(ciphertext,key)
	print('The plaintext based on the above key is:')
	print(plaintext)

if __name__ == '__main__':
	main()





