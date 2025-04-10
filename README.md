# List of all cryptography hash algorithms

#### In this repository, I will state 
1) How to code for all the common cryptography algorithms?
2) How to code the RSA algorithm?
3) What are the scopes and features for cryptography?

## How to code for all the common cryptography algorithms?
#### The common hashes to be ever known for a basic cryptographer is : 
- SHA, SHA 2, SHA 3
- MD5
- AES
- DES
- RSA
- Diffie Hellman

#### SHA, SHA 2 and SHA 3
SHA (Secure Hash Algorithm) is used to generate unique fixed-length digital input data known as hashes. SHA variations such as SHA-2 and SHA-3 are commonly used to ensure data integrity.

How to code SHA 3 in Python?
There is a direct library for it called hashlib which can easliy create a hash based on the cryptographic algorithm.
```bash
import hashlib

def sha3_hash(data, hash_bits):
    
    if isinstance(data, str):
        data = data.encode('utf-8')

    if hash_bits == 224:
        hash_object = hashlib.sha3_224(data)
    elif hash_bits == 256:
        hash_object = hashlib.sha3_256(data)
    elif hash_bits == 384:
        hash_object = hashlib.sha3_384(data)
    elif hash_bits == 512:
        hash_object = hashlib.sha3_512(data)
    else:
        raise ValueError("Invalid hash_bits. Must be 224, 256, 384, or 512.")

    return hash_object.hexdigest()

# Example usage
data_to_hash = input("Give me a string: ")

hash_256 = sha3_hash(data_to_hash, 256)
hash_384 = sha3_hash(data_to_hash, 384)

print(f"SHA-3-256 hash: {hash_256}")
print(f"SHA-3-384 hash: {hash_384}")
````
Through this code, we can easily find out the hash values of the algorithm.

#### MD5
MD5 (Message-Digest) is a cryptographic hash function algorithm that takes the message as input of any length and changes it into a fixed-length message of 16 bytes. 

How to code MD5 in Python?
There is a direct library for it called hashlib which can easliy create a hash based on the cryptographic algorithm.

```bash
import hashlib

str2hash = input("Enter the string you want encrypted : ")
result = hashlib.md5(str2hash.encode())
print("MD5 hash: ",result.hexdigest())
````
Through this code, we can easily find out the hash values of this algorithm.

#### AES
AES (Advanced Encryption Standard) is a popular encryption algorithm which uses the same key for encryption and decryption.
It is a symmetric cipher algorithm with block size of 128 bits, 192 bits or 256 bits.

How to code AES in Python?
There is a direct library for it called hashlib which can easliy create a hash based on the cryptographic algorithm.

```bash
import hashlib

str2hash = input("Enter the string you want encrypted : ")
result = hashlib.md5(str2hash.encode())
print("MD5 hash: ",result.hexdigest())
````
Through this code, we can easily find out the hash values of this algorithm.

