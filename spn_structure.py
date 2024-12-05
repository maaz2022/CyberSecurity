def xor_with_key(data, key):
    return ''.join(str(int(data[i]) ^ int(key[i])) for i in range(len(data)))

# Example input and key
data = '1010'
key = '1101'

# XOR operation
result = xor_with_key(data, key)
print(f"Result after XOR: {result}")
