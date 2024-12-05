from collections import Counter

def frequency_analysis(ciphertext):
    frequencies = Counter(ciphertext)
    return frequencies.most_common()

ciphertext = "GDKKN VNQKC"  # Encrypted version of "HELLO WORLD"
freq = frequency_analysis(ciphertext)
print("Letter Frequency Analysis:", freq)
