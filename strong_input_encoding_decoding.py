import html

# Example of potentially malicious user inputs
user_inputs = [
    "<script>alert('XSS Attack!');</script>",  # Malicious JavaScript
    "<img src='nonexistent.jpg' onerror='alert(\"Hacked!\")'>",  # Injected image tag with malicious script
    "Hello <b>World</b> & Welcome!",  # Innocent but includes HTML tags and special characters
]

# Encoding user inputs to make them safe for display on a webpage
print("Encoding potentially harmful user inputs:\n")
encoded_inputs = []
for i, input_text in enumerate(user_inputs, 1):
    encoded_text = html.escape(input_text)  # Encode special characters
    encoded_inputs.append(encoded_text)
    print(f"Input {i}:")
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_text}\n")

# Decoding encoded inputs back to their original form
print("Decoding back the encoded inputs:\n")
for i, encoded_text in enumerate(encoded_inputs, 1):
    decoded_text = html.unescape(encoded_text)  # Decode back to the original form
    print(f"Encoded {i}: {encoded_text}")
    print(f"Decoded: {decoded_text}\n")
