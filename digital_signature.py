import struct
import random


# Helper functions for SHA-1
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


def sha1(data):
    # Initialize constants
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Pre-processing: Padding
    data_len = len(data)
    ml = data_len * 8
    data += b'\x80'
    while len(data) % 64 != 56:
        data += b'\x00'
    data += struct.pack('>Q', ml)

    # Process the message in 512-bit chunks
    for i in range(0, len(data), 64):
        chunk = data[i:i + 64]
        words = [
            struct.unpack('>I', chunk[j:j + 4])[0] for j in range(0, 64, 4)
        ]

        for j in range(16, 80):
            words.append(
                left_rotate(
                    words[j - 3] ^ words[j - 8] ^ words[j - 14]
                    ^ words[j - 16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + words[j] & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Concatenate the hash components
    hash_hex = f'{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}'
    return hash_hex


# Simplified DSA parameters (for educational purposes only)
p = 23  # A prime number
q = 11  # A prime divisor of p-1
g = 6  # A generator modulo p

# Key generation (usually done once)
private_key = random.randint(1, q - 1)
public_key = pow(g, private_key, p)


# Signing
def sign(message, private_key):
    k = random.randint(1, q - 1)
    r = pow(g, k, p) % q
    inv_k = pow(k, -1, q)
    hash_value = int(sha1(message.encode('utf-8')), 16)
    s = (inv_k * (hash_value + private_key * r)) % q
    return (r, s)


# Verification
def verify(message, signature, public_key):
    r, s = signature
    if not (0 < r < q and 0 < s < q):
        return False

    w = pow(s, -1, q)
    hash_value = int(sha1(message.encode('utf-8')), 16)
    u1 = (hash_value * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(public_key, u2, p) % p) % q

    return v == r


# Example usage
message = "Hello, DSA!"
signature = sign(message, private_key)
print("Signature:", signature)
valid = verify(message, signature, public_key)
print("Signature is valid:", valid)
