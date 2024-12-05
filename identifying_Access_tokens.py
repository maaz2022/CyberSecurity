import requests

token = "your_valid_access_token"
headers = {'Authorization': f'Bearer {token}'}
response = requests.get("https://api.github.com/user", headers=headers)

print(response.json())
