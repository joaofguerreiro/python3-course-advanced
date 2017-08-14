"""
One of the most popular uses of hashes is storing the hash of a password instead of the 
password itself.
"""
import hashlib
md5 = hashlib.md5()
# To use the md5 hash, you have to pass it a byte string instead of a regular string

# md5.update('Python rocks!')
# Traceback (most recent call last):
#   File "hashing_sample.py", line 7, in <module>
#     md5.update('Python rocks!')
# TypeError: Unicode-objects must be encoded before hashing

# MD5 is the weakest of all the hashing methods.
md5.update(b'Python rocks!')
print (md5.digest())
# b'\x14\x82\xec\x1b#d\xf6N}\x16*+[\x16\xf4w'

# Generates a hash made of hexadecimals
print (md5.hexdigest())
# 1482ec1b2364f64e7d162a2b5b16f477

# We can create our hash instance and call its digest method at the same time.
sha = hashlib.sha1(b'Hello Python').hexdigest()
print (sha)
# 422fbfbc67fe17c86642c5eaaa48f8b670cbed1b


# *------ KEY DERIVATION ------*
import binascii
"""
Password-based key derivation function 2 (pbkdf2), it uses HMAC as its psuedorandom function.

A salt is random data used as an additional input to a one-way function that "hashes" a password or passphrase.
The primary function of salts is to defend against dictionary attacks.
"""
dk = hashlib.pbkdf2_hmac(
	hash_name='sha256',  # we create a SHA256 hash on a password using a lousy salt but with 100,000 iterations
	password=b'bad_password34',
	salt=b'bad_salt',
	iterations=10000
	)  # SHA is not recommended for creating keys of passwords
print (binascii.hexlify(dk))
#  b'7f78f6d8aa1126da9f2e36993c6462cca81bedd69613ebab6da5de519ef2f217'
