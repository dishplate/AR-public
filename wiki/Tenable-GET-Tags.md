
Here’s a Python script that retrieves all tags and their details from Tenable.io (cloud.tenable.com) using the Tenable.io API. It utilizes the requests library to interact with the API.

You’ll need:
	1.	Your Tenable.io API Key (access_key and secret_key).
	2.	The correct API endpoint (https://cloud.tenable.com/tags).

Python Script: Fetch Tags from Tenable.io
~~~
import requests

# Replace with your actual Tenable.io API credentials
ACCESS_KEY = "your_access_key"
SECRET_KEY = "your_secret_key"

# API Endpoint
BASE_URL = "https://cloud.tenable.com"
TAGS_ENDPOINT = f"{BASE_URL}/tags"

# Headers for authentication
HEADERS = {
    "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY}",
    "Accept": "application/json"
}

def fetch_tags():
    """Fetches all tags from Tenable.io."""
    tags = []
    try:
        response = requests.get(TAGS_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        tags = response.json().get('tags', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tags: {e}")
    return tags

if __name__ == "__main__":
    all_tags = fetch_tags()
    if all_tags:
        for tag in all_tags:
            print(f"Tag ID: {tag.get('uuid')}, Name: {tag.get('category')}/{tag.get('value')}")
    else:
        print("No tags found.")
~~~
How It Works:
	•	It sends a GET request to https://cloud.tenable.com/tags to fetch all tags.
	•	The API response includes tag UUIDs, categories, values, and metadata.
	•	The script prints Tag ID, Category, and Value.

Prerequisites:
	1.	Install requests if not already installed:

pip install requests


	2.	Replace your_access_key and your_secret_key with your Tenable.io API credentials.