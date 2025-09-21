from Crypto.Cipher import AES, ARC4, ChaCha20
from Crypto.Random import get_random_bytes


# AES Encryption/Decryption
aes_key = get_random_bytes(32)        
aes_iv = get_random_bytes(16)         
plaintext = b"HELLO WORLD"

# AES in CBC padding
pad_len = 16 - (len(plaintext) % 16)
padded_plaintext = plaintext + bytes([pad_len]*pad_len)

aes_cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
aes_ciphertext = aes_cipher.encrypt(padded_plaintext)
print("AES Ciphertext:", aes_ciphertext.hex())

# Decrypt
aes_decipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
decrypted = aes_decipher.decrypt(aes_ciphertext)
decrypted = decrypted[:-decrypted[-1]]  #padding
print("AES Decrypted:", decrypted.decode())


# RC4 Encryption/Decryption
rc4_key = get_random_bytes(16)        
rc4_cipher = ARC4.new(rc4_key)
rc4_ciphertext = rc4_cipher.encrypt(plaintext)
print("RC4 Ciphertext:", rc4_ciphertext.hex())

# Decrypt
rc4_decipher = ARC4.new(rc4_key)
rc4_decrypted = rc4_decipher.decrypt(rc4_ciphertext)
print("RC4 Decrypted:", rc4_decrypted.decode())


# ChaCha20 Encryption/Decryption
chacha_key = get_random_bytes(32)     
chacha_nonce = get_random_bytes(12)  

chacha_cipher = ChaCha20.new(key=chacha_key, nonce=chacha_nonce)
chacha_ciphertext = chacha_cipher.encrypt(plaintext)
print("ChaCha20 Ciphertext:", chacha_ciphertext.hex())

# Decrypt
chacha_decipher = ChaCha20.new(key=chacha_key, nonce=chacha_nonce)
chacha_decrypted = chacha_decipher.decrypt(chacha_ciphertext)
print("ChaCha20 Decrypted:", chacha_decrypted.decode())
