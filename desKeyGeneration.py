# write a program to perform left rotate in des on key and generate 16 keys


# Initial 64-bit DES key (56 bits used for actual key)
initial_key = 0x133457799BBCDFF1

# Define the number of bits to rotate left in each round
bit_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# Function to perform left rotation on a 28-bit value
def left_rotate(value, shift):
    return ((value << shift) | (value >> (28 - shift))) & 0xFFFFFFF


# Split the 56-bit initial key into two 28-bit halves
left_half = (initial_key >> 28) & 0xFFFFFFF
right_half = initial_key & 0xFFFFFFF

subkeys = []

# Generate 16 subkeys
for i in range(16):
    # Perform left rotation on both halves
    left_half = left_rotate(left_half, bit_shifts[i])
    right_half = left_rotate(right_half, bit_shifts[i])

    # Combine the halves and apply a 48-bit compression to generate the subkey
    subkey = ((left_half << 28) | right_half) & 0xFFFFFFFFFFFFF
    subkeys.append(subkey)

    print(f"Subkey {i + 1}: {subkey:012X}")
