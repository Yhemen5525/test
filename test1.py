import requests

def fetch_dummy_data():
    url = 'https://jsonplaceholder.typicode.com/posts'  # URL to fetch dummy data (posts)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error occurred while fetching data:', response.status_code)

# Fetch dummy data and print it
dummy_data = fetch_dummy_data()
if dummy_data:
    for item in dummy_data:
        print(item)