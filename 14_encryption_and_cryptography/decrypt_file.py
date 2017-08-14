from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


code = 'nooneknows'

with open('encrypted_data.bin', 'rb') as fobj:
	# when you import the private key, you must give it your passcode
	private_key = RSA.import_key(open('my_private_rsa_key.bin').read(), passphrase=code)  # we import our private key

	# Reads in the private key first, then the next 16 bytes for the nonce, which is followed by 
	# the next 16 bytes which is the tag and finally the rest of the file, which is our data.
	enc_session_key, nonce, tag, ciphertext = [
		fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
	]

	cipher_rsa = PKCS1_OAEP.new(private_key)
	session_key = cipher_rsa.decrypt(enc_session_key)  # decrypts our session key

	cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)  # recreates our AES key
	data = cipher_aes.decrypt_and_verify(ciphertext, tag)  # decrypts the data

print (data)
# b'blah blah blah Python blah blah'
