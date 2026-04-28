

```
import requests
import json
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API endpoint and site ID
base_url = "https://<INSIGHTVM_INSTANCE_URL>:3780/api/3"
site_id = "<SITE_ID>"  # Replace with your site code

# Basic authentication credentials
username = "<YOUR_USERNAME>"
password = "<YOUR_PASSWORD>"

# Endpoint to get site details
url = f"{base_url}/sites/{site_id}"

# Make the GET request
response = requests.get(url, auth=(username, password), verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Print raw JSON response
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error: {response.status_code}, {response.text}")
```