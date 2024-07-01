import requests

def test_api():
    # Specify the API endpoint URL
    api_url = "https://jsonplaceholder.typicode.com/todos/1"

    # Make a GET request
    response = requests.get(api_url)

    # Check the response status code
    if response.status_code == 200:
        # Print the response content
        print("API Response:")
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_api()


import requests

def test_post_api():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(api_url, json=data)

    if response.status_code == 201:
        print("Post Created Successfully!")
        print("Post ID:", response.json()["id"])
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_post_api()

