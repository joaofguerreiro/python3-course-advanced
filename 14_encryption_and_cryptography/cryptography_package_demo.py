"""
The Fernet module implements an easy-to-use authentication scheme that uses a symmetric 
encryption algorithm which guarantees that any message you encrypt with it cannot be 
manipulated or read without the key you define.
"""
from cryptography.fernet import Fernet

cipher_key = Fernet.generate_key()  # generates a Fernet key
print (cipher_key)
# b'xoQyjFBJOwLkZ3SfHdzCYK93DDvUWh_aLiqhR0Yd6o0='

cipher = Fernet(cipher_key)  # creates Fernet cipher instance using our key
text = b'My super secret message'  # data to be encrypted/decrypted
encrypted_text = cipher.encrypt(text)  # encrypts data using Fernet cipher
print (encrypted_text)
# b'gAAAAABZjds9L7WReFpjKbVJ6XCUoaMFF-m8O7T80g_iXII0R_oBBlKvxW8RL\
# zGOO8QvS8QmMZGP8u-96iXScGvVcxZj1k26OOaRBmJ-rXBx8vhEMO0yDmM='

decrypted_text = cipher.decrypt(encrypted_text)  # decrypts data using Fernet cipher
print (decrypted_text)
# b'My super secret message'
