import random

# Function to perform Diffie-Hellman key exchange
def diffie_hellman(p, g):
    # Generate private keys
    a = random.randint(1, p - 1)  # Alice's private key
    b = random.randint(1, p - 1)  # Bob's private key

    # Generate public keys
    A = pow(g, a, p)  # Alice's public key
    B = pow(g, b, p)  # Bob's public key

    # Generate shared secret keys
    shared_secret_A = pow(B, a, p)  # Alice's shared secret key
    shared_secret_B = pow(A, b, p)  # Bob's shared secret key

    # Check if the shared secrets match
    assert shared_secret_A == shared_secret_B

    return shared_secret_A

# Accepting user input for p and g
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root modulo p (g): "))

shared_secret = diffie_hellman(p, g)
print("Shared secret key:", shared_secret)
