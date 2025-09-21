from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# RSA key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

message = b"HELLO"

# Encryption - public key
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)
print("RSA Ciphertext:", ciphertext.hex())

# Decryption - private key
decipher = PKCS1_OAEP.new(private_key)
decrypted = decipher.decrypt(ciphertext)
print("RSA Decrypted:", decrypted.decode())
