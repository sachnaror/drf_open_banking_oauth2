import requests

url = "http://127.0.0.1:8000/o/authorize/"
params = {
    "client_id": "mth7EayOlmF5kAiwAd5zwOqKVMmfVslkjQkJoOMO",
    "response_type": "code",
    "redirect_uri": "http://localhost/callback/"
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.text)  # Print response for debugging
