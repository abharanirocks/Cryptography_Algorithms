import struct

#implement initialization step of SHA-1 preparation of buffer of length 1024

# Initial hash values (as 160-bit hexadecimal numbers)
h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0

# Initialize the message buffer with zeros
message_buffer = [0] * 64


# Function to prepare the message buffer with the input data
def prepare_message_buffer(input_data):
    # Convert the input data into a binary format (bytes)
    input_data_bytes = input_data.encode('utf-8')

    # Get the length of the input data in bits
    data_length_bits = len(input_data_bytes) * 8

    # Initialize the message buffer with zeros
    message_buffer = [0] * 64

    # Set the first 64 bits of the message buffer to the data length in bits
    message_buffer[0:8] = struct.unpack(">8B",
                                        struct.pack(">Q", data_length_bits))

    # Place the input data into the message buffer
    for i in range(len(input_data_bytes)):
        message_buffer[i + 8] = input_data_bytes[i]

    return message_buffer


# Example usage:
input_data = "Network And Cyber Security"
message_buffer = prepare_message_buffer(input_data)

# Print the initial hash values and the prepared message buffer
print("Initial Hash Values:")
print(f"h0: {h0:08x}")
print(f"h1: {h1:08x}")
print(f"h2: {h2:08x}")
print(f"h3: {h3:08x}")
print(f"h4: {h4:08x}")

print("\nMessage Buffer:")
for i in range(0, len(message_buffer), 8):
    print(" ".join(f"{message_buffer[j]:02x}" for j in range(i, i + 8)))
