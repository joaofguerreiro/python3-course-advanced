from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


with open('encrypted_data.bin', 'wb') as out_file:
	recipient_key = RSA.import_key(open('my_rsa_public.pem').read())  # imports our public key
	session_key = get_random_bytes(16)  # creates a 16-byte session key

	# hybrid encryption method - PKCS#1 OAEP (Optimal asymmetric encryption padding)
	cipher_rsa = PKCS1_OAEP.new(recipient_key)
	out_file.write(cipher_rsa.encrypt(session_key))

	cipher_aes = AES.new(session_key, AES.MODE_EAX)  # AES cipher
	data = b'blah blah blah Python blah blah'
	ciphertext, tag = cipher_aes.encrypt_and_digest(data)  # encrypts the data

	# Nonce is an arbitrary number that is only used for crytographic communication and are
	# usually random or pseudorandom numbers.
	out_file.write(cipher_aes.nonce)
	out_file.write(tag)
	out_file.write(ciphertext)
