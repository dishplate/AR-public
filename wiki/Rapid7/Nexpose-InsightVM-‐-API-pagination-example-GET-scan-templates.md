~~~
#2024-12-05 This works, including pagination
#I would prefer a different way of pagination...I have to figure that out.
import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
import os
from dotenv import load_dotenv
import pandas as pd

# Load credentials from .env file
load_dotenv()
username = os.getenv("username1")
password = os.getenv("password2")

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

console_url = "https://ivm_console"
url = f'{console_url}/api/3/sites'

# Function to get all pages of sites
def get_all_sites(url, auth):
    sites = []
    params = {'page': 0, 'size': 100}  # Adjust page size as needed
    while True:
        response = requests.get(url, auth=auth, params=params, verify=False)
        if response.status_code == 200:
            data = response.json()
            sites.extend(data['resources'])
            if params['page'] >= data['page']['totalPages'] - 1:
                break
            params['page'] += 1
        else:
            print(f'Failed to retrieve sites: {response.status_code}')
            print(response.text)
            break
    return sites

# Make the request
sites = get_all_sites(url, HTTPBasicAuth(username, password))

# Print all site names retrieved
print("All Site Names Retrieved:")
site_data = []
for site in sites:
    site_name = site.get("name", "N/A")
    site_id = site.get("id", "N/A")
    scan_template = site.get("scanTemplate", "N/A")
    print(f'Site ID: {site_id}, Name: {site_name}, scanTemplate: {scan_template}')
    site_data.append({'Site ID': site_id, 'Name': site_name, 'Scan Template': scan_template})

# Save the results to a CSV file
output_df = pd.DataFrame(site_data)
output_df.to_csv(r'C:/code/code/site_templates.csv', index=False)

print("Site data saved to site_templates.csv.")
















~~~