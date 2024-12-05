def spn_round(data, s_box, p_box, round_key):
    """
    Performs one round of an SPN.
    - Substitution: Use an S-Box to transform the input.
    - Permutation: Rearrange the bits using a P-Box.
    - Key Mixing: XOR with the round key.
    """
    # Substitution
    substituted_data = ''.join(s_box[data[i:i+2]] for i in range(0, len(data), 2))

    # Permutation
    permuted_data = ''.join(substituted_data[i] for i in p_box)

    # Key Mixing
    mixed_data = ''.join(str(int(permuted_data[i]) ^ int(round_key[i])) for i in range(len(permuted_data)))
    return mixed_data

# Example S-Box, P-Box, and round key
s_box = {'00': '11', '01': '10', '10': '01', '11': '00'}
p_box = [3, 0, 2, 1]  # Simple permutation
round_key = '1101'

# Input data
data = '1010'
result = spn_round(data, s_box, p_box, round_key)
print(f"SPN Round Output: {result}")
