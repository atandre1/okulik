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
