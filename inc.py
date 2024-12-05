import requests

# Define proxy details (replace with valid working proxy)
# Replace 'username', 'password', 'yourproxy.com', and 'port' with actual details
proxies = {
    "http": "http://yourproxy.com:8080",  # Replace with valid proxy server
    "https": "https://yourproxy.com:8080"  # Replace with valid proxy server
}

# URL of the site you want to access via proxy
url = "http://example.com"  # You can change this to any other testable URL

# Sending request through proxy with a timeout
try:
    response = requests.get(url, proxies=proxies, timeout=10)  # Timeout set to 10 seconds
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    print("Request succeeded through proxy!")
    print(response.text[:500])  # Print the first 500 characters of the response content
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.ProxyError:
    print("There was an issue connecting to the proxy.")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# TEST WITHOUT PROXY
# If you want to verify that the internet connection and the target URL work, use this:
try:
    response = requests.get(url, timeout=10)  # Access without proxy
    response.raise_for_status()  # Check if the request succeeded
    print("Request succeeded without proxy!")
    print(response.text[:500])  # Print the first 500 characters of the response content
except requests.exceptions.RequestException as e:
    print(f"Request without proxy failed: {e}")
