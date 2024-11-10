import struct
from math import sin

def left_rotate(value, amount):
    return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF

def md5(message):
    # Initial hash values
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Preprocessing: padding the message
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    message += struct.pack('<Q', original_bit_len)

    # Constants
    K = [int(abs((1 << 32) * sin(i + 1))) for i in range(64)]
    S = [7, 12, 17, 22] * 4

    # Process each 512-bit chunk
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        words = list(struct.unpack('<16I', chunk))

        # Initialize hash value for this chunk
        A, B, C, D = a, b, c, d

        # Main loop
        for j in range(64):
            if j < 16:
                f = (B & C) | (~B & D)
                g = j
            elif j < 32:
                f = (D & B) | (~D & C)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                f = C ^ (B | ~D)
                g = (7 * j) % 16
            
            f = (f + A + K[j] + words[g]) & 0xFFFFFFFF
            A, D, C, B = D, (B + left_rotate(f, S[j % 4])) & 0xFFFFFFFF, B, C

        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF

    # Produce final hash value (little-endian)
    return (a, b, c, d)


text = input("Enter a String to Hash: ").encode('utf-8')
hash_values = md5(text)
print("MD5 Hash:", ''.join(f'{val:02x}' for val in hash_values))