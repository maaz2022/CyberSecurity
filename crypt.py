aes_sbox = [
    [0x63, 0x7C, 0x77, 0x7B],  # Partial S-Box
    [0x6B, 0x6F, 0xC5, 0x30]
]
row, col = 1, 2  # Example input nibbles
substituted = aes_sbox[row][col]
print("S-Box Output:", hex(substituted))
