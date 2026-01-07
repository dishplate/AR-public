```
#This works, but has some error too
import requests
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL verification warnings (optional)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Replace with your Nexpose credentials
nexpose_username = 'xxx'
nexpose_password = 'xxx'

# Encode the credentials to Base64
credentials = base64.b64encode(f'{nexpose_username}:{nexpose_password}'.encode('utf-8')).decode('utf-8')

# Replace with your Nexpose console address
console_address = 'https://172.221.212.72:3780'

# Replace with your site ID
site_id = '1'

# Set up the API endpoint for assets in a site
api_endpoint = f'{console_address}/api/3/sites/{site_id}/assets'

# Set up headers with the Base64 encoded credentials
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {credentials}'
}

try:
    # Make a GET request to the API
    response = requests.get(api_endpoint, headers=headers, verify=False)

    # Print the raw response content for debugging
    print("Raw Response Content:")
    print(response.text)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        assets = response.json()

        # Print the list of assets
        for asset in assets:
            print(f"Asset ID: {asset['id']}, IP Address: {asset['ip']}, OS: {asset['os']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
!!!