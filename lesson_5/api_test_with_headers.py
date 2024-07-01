import requests

def test_headers_and_params():
    api_url = "https://api.example.com/data"
    headers = {"Content-Type": "application/json"}
    params = {"param1": "value1", "param2": "value2"}

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        print("API Response:")
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_headers_and_params()
