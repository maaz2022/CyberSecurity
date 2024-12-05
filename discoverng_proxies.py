import requests

# Define your proxy details
proxies = {
    "http": "http://yourproxy.com:8080",  # Replace with actual working proxy
    "https": "https://yourproxy.com:8080"
}

# URL of the site you want to access via proxy
url = "http://example.com"

# Sending request through proxy
try:
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    print("Request succeeded through proxy!")
    print(response.text[:500])  # Printing first 500 characters of the response
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
