from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.exceptions import InvalidSignature

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

def sign_message(msg):
    return private_key.sign(msg, hashes.SHA256())

def verify_signature(msg, sig):
    try:
        public_key.verify(sig, msg, hashes.SHA256())
        return "Signature is valid."
    except InvalidSignature:
        return "Signature is invalid."

message = input("Enter the message to sign: ").encode()
signature = sign_message(message)
print(f"Signature: {signature.hex()}")
print(verify_signature(message, signature))
