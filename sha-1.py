import struct

def sha1(data):
    # Initialize constants
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Pre-processing: Padding the input data
    ml = len(data) * 8  # Message length in bits
    data += b'\x80'  # Append a single '1' bit to the end of the data
    while (len(data) * 8) % 512 != 448:
        data += b'\x00'  # Pad with zeros until message length % 512 == 448

    # Append the original message length as a 64-bit big-endian integer
    data += struct.pack('>Q', ml)

    # Process the message in 512-bit blocks
    for i in range(0, len(data), 64):
        chunk = data[i:i + 64]

        # Break the chunk into 16 32-bit big-endian words
        w = list(struct.unpack('>16I', chunk))

        # Extend the 16 words into 80 words
        for j in range(16, 80):
            w.append(rotate_left(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1))

        # Initialize hash values for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for j in range(80):
            if 0 <= j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (rotate_left(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = rotate_left(b, 30)
            b = a
            a = temp

        # Update hash values for this chunk
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Concatenate the hash values
    hash_hex = '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)
    return hash_hex

def rotate_left(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

# Test the SHA-1 function
if __name__ == "__main__":
    input_string = "Hello"
    sha1_hash = sha1(input_string.encode())
    print("SHA-1 Hash:", sha1_hash)
