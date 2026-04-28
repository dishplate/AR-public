~~~
#2024-12-04 This works to show all scan engines and exclude some that are defined in excluded_sites variable
import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
import maskpass  # importing maskpass library

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Credentials
username = "name123"
password = maskpass.askpass(prompt="Password:", mask="#")
console_url = "https://nexpose123:3780"

# API endpoint for scan engines
url = f'{console_url}/api/3/scan_engines'

excluded_log = []
# List of site IDs to exclude
excluded_sites = {3: 'Local scan engine', 131: 'description'}  # Replace with your site IDs and names

# Make the request
response = requests.get(url, auth=(username, password), verify=False)
if response.status_code == 200:
    engines = response.json()['resources']
    for engine in engines:
        engine_id = engine['id']
        engine_name = engine['name']
        engine_status = engine['status']
        # engine_prod_version = engine.get['productVersion','N/A'] Don't know why this isn't working
        engine_version = engine.get('contentVersion','N/A')

        # Skip engines belonging to excluded sites
        if engine_id in excluded_sites:
            excluded_log.append(f'Skipped: Engine ID {engine_id} (Site ID {engine_id}: {excluded_sites[engine_id]})')
            continue


        print(f'ID: {engine_id}, Name: {engine_name}, content_Version: {engine_version}, engine_status: {engine_status},')

    # Log excluded sites at the end
    print("\nExcluded Engines:")
    for log_entry in excluded_log:
        print(log_entry)

else:
    print(f'Failed to retrieve engines: {response.status_code}')
    print(response.text)
~~~