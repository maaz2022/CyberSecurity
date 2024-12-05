import html

user_input = "<script>alert('XSS');</script>"
encoded_input = html.escape(user_input)
print(encoded_input)
