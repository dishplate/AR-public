~~~
#This works as is. 11/14/2024
#Go to https://nexpose.local/3780/api/3/assets in firefox to see the schema breakdown
import requests
import base64
import pandas as pd
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL verification warnings (optional)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Replace with your Nexpose credentials
nexpose_username = 'xxxx'
nexpose_password = 'xxxxx'

# Encode the credentials to Base64
credentials = base64.b64encode(f'{nexpose_username}:{nexpose_password}'.encode('utf-8')).decode('utf-8')

# Replace with your Nexpose console address
console_address = 'https://xxxxx:3780'

# Replace with your site ID
site_id = '1'

# Set up the API endpoint for assets in a site
# api_endpoint = f'{console_address}/api/3/sites/{site_id}/assets'
# 
api_endpoint =  f'{console_address}/api/3/assets' 

# Set up headers with the Base64 encoded credentials
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {credentials}'
}

try:
    # Make a GET request to the API
    response = requests.get(api_endpoint, headers=headers, verify=False)

    # Print the raw response content for debugging
    #print("Raw Response Content:")
    # print(response.text)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        r = response.json()
        # Try to parse the JSON response
        try:
            # Process each asset
            for asset in r['resources']:
                # addresses = addresses.get('assessedForVulnerabilities')
                asset_ip = asset.get('ip')
                asset_hostname = asset.get('hostName', 'N/A')
                asset_riskscore = asset.get('riskScore')
                asset_vulns = asset.get('vulnerabilities[total]')
                print(asset_hostname, asset_ip, "#", asset_riskscore,"#", asset_vulns)


            
            # for hostnames in r:
            #     print(r['resources'][0]['hostName'])
            # print('###############################')
            # print(assets['resources'][0]['hostName'])
            # print(assets['resources'][0]['ip'])
            # print(assets['resources'][0]['mac'])
            # print('###############################')
            # json_data = json.dumps(assets, indent=4)        
            # print(json_data['resources']['addresses']['ip'])              

        except ValueError as ve:
            print(f"Error parsing JSON response: {ve}")

    else:
        print(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
###############################################################################






~~~