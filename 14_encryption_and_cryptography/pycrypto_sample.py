from Crypto.Cipher import DES
"""
Key size for DES encryption is 8 bytes.
"""

key = b'abcdefgh'
def pad(text):
	"""
	Pad any string out with spaces until it’s a multiple of 8.
	The string that we will be encrypting must be a multiple of 8 in length.
	"""
	while len(text) % 8 != 0:
		text += b' '
	return text

des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)

# Raises an error because it cannot encrypt a byte string that isn't a multiple of 8.
# encrypted_text = des.encrypt(text)
# Traceback (most recent call last):
#   File "/usercode/__ed_file.py", line 10, in <module>
#     encrypted_text = des.encrypt(text)
#   File "/usr/local/lib/python3.5/dist-packages/Crypto/Cipher/_mode_ecb.py", line 124, in encrypt
#     raise ValueError("Error %d while encrypting in ECB mode" % result)
# ValueError: Error 3 while encrypting in ECB mode

encrypted_text = des.encrypt(padded_text)
print (encrypted_text)
# b'>\xfc\x1f\x16x\x87\xb2\x93\x0e\xfcH\x02\xd59VQ'

# Now, onto decrypting this string:
print (des.decrypt(encrypted_text))
# b'Python rocks!   '


"""
Creating a RSA key
RSA is one of the strongest encryption algorithms
"""
from Crypto.PublicKey import RSA

code = 'nooneknows'
key = RSA.generate(2048)  # generates an RSA key instance of 2048 bits
encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")  # Generates private key
with open('my_private_rsa_key.bin', 'wb') as f:
	f.write(encrypted_key)
with open('my_rsa_public.pem', 'wb') as f:
	f.write(key.publickey().exportKey())  # Generates the public key
