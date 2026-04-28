Untested code from chatGPT
~~~

import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

INSIGHTVM_CONSOLE = os.getenv("INSIGHTVM_CONSOLE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Replace this with your hostname or IP
TARGET_HOSTNAME = "example-hostname"

# Function to fetch the site ID from hostname or IP
def get_site_id(target):
    url = f"{INSIGHTVM_CONSOLE}/api/3/sites"
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers, auth=(USERNAME, PASSWORD), verify=False)
    if response.status_code == 200:
        sites = response.json()["resources"]
        for site in sites:
            site_id = site["id"]
            site_assets = get_site_assets(site_id)
            for asset in site_assets:
                if asset.get("host-name") == target or asset.get("ip-address") == target:
                    return site_id
    else:
        print(f"Error: Unable to fetch sites ({response.status_code}).")
    return None

# Function to fetch assets for a site
def get_site_assets(site_id):
    url = f"{INSIGHTVM_CONSOLE}/api/3/sites/{site_id}/assets"
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers, auth=(USERNAME, PASSWORD), verify=False)
    if response.status_code == 200:
        return response.json()["resources"]
    return []

# Function to get credential status messages for a given asset
def get_credential_status(asset_id):
    url = f"{INSIGHTVM_CONSOLE}/api/3/assets/{asset_id}/credentials"
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers, auth=(USERNAME, PASSWORD), verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch credential status ({response.status_code}).")
        return None

# Main
site_id = get_site_id(TARGET_HOSTNAME)
if site_id:
    print(f"Found site ID: {site_id}")
    site_assets = get_site_assets(site_id)
    for asset in site_assets:
        if asset.get("host-name") == TARGET_HOSTNAME or asset.get("ip-address") == TARGET_HOSTNAME:
            asset_id = asset["id"]
            credential_status = get_credential_status(asset_id)
            if credential_status:
                print(json.dumps(credential_status, indent=4))
else:
    print("Target hostname or IP not found.")


~~~