import random

def diffie_hellman(p, g):
    a = random.randint(1, p - 1)
    b = random.randint(1, p - 1)
    A = pow(g, a, p)
    B = pow(g, b, p)
    shared_secret_A = pow(B, a, p)
    shared_secret_B = pow(A, b, p)
    assert shared_secret_A == shared_secret_B
    return shared_secret_A

p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root modulo p (g): "))

shared_secret = diffie_hellman(p, g)
print("Shared secret key:", shared_secret)
