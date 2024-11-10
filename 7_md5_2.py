import hashlib

def generate_md5_hash(inputString):
    hash = hashlib.md5(inputString.encode())
    output = hash.hexdigest()
    return output

inputString = input("Enter a Message to Hash: ")
print("MD5 Hash of the input string:", end="")
print(generate_md5_hash(inputString))