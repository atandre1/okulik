import requests
from requests.auth import HTTPBasicAuth

def test_authenticated_api():
    api_url = "https://api.example.com/data"
    username = "your_username"
    password = "your_password"

    response = requests.get(api_url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        print("Authenticated API Response:")
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_authenticated_api()
