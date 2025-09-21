import hashlib

message = "HELLO WORLD".encode()

hash_algorithms = ["md5","sha1","sha224","sha256","sha384","sha512","sha3_224","sha3_256","sha3_384","sha3_512","blake2b","blake2s"]

print("Input Message:", message.decode(), "\n")

for algo in hash_algorithms:
    h = hashlib.new(algo)
    h.update(message)
    print(f"{algo.upper():<10} → {h.hexdigest()}")
