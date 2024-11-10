import hashlib

def generate_sha512_hash(inputString):
    hash = hashlib.sha512(inputString.encode())
    output = hash.hexdigest()
    return output

inputString = input("Enter a Message to Hash: ")
print("SHA-512 Hash of the Input String: ", end="")
print(generate_sha512_hash(inputString))

