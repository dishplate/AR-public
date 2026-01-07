~~~
#11/1/24
#This works
#Script to show site at a high level. Just change the site ID in line 13
import requests
import json
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API endpoint and site ID
base_url = "https://nexposesite:3780/api/3"
site_id = "1"  # Replace with your site code

# Basic authentication credentials
username = "xxx"
password = "xxx"

def get_ivm_data(name):
    # Endpoint to get site details
    url = f"{base_url}/sites/{site_id}"
    # Make the GET request
    response = requests.get(url, auth=(username, password), verify=False)
    

    if response.status_code == 200:
        response_data = response.json()
        return response_data
        print("data retrieved")
    if response.status_code != 200:
        print("You have a problem")

site_data = "assets"
DATA1 = get_ivm_data(site_data)

if DATA1:
    print(f"Site Name: {DATA1["name"]}")
    print(f"Site ID: {DATA1["id"]}")
    print(f"Asets in site: {DATA1["assets"]}")
    print(f"Last scan time: {DATA1["lastScanTime"]}")

~~~