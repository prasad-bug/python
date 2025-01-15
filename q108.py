import requests

# Example API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Fetch data from the API
response = requests.get(url)

# Print part of the JSON response
if response.status_code == 200:
    data = response.json()
    print("Data fetched from API:")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
