from collections import Counter

def frequency_analysis(ciphertext):
    frequencies = Counter(ciphertext)
    return frequencies.most_common()

ciphertext = "GDKKN VNQKC"  # Ciphertext of "HELLO WORLD"
freq = frequency_analysis(ciphertext)
print("Frequency Analysis:", freq)
