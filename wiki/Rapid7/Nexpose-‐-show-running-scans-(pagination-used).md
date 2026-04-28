~~~
#issues: the script is not working as expected. It's supposed to show running scans but is also showing finished scans.
#The last line also says "No scans running" even though there are running scans.
import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
from collections import Counter
import maskpass  # importing maskpass library

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Credentials
username = maskpass.askpass(prompt="Username:", mask="#")
password = maskpass.askpass(prompt="Password:", mask="#")
console_url = "https://xxx:3780"

# API endpoint for running scans
url = f'{console_url}/api/3/scans'

# Function to get all pages of scans starting from the most recent
def get_all_scans(url, auth):
    scans = []
    params = {'page': 1, 'size': 100, 'sort': 'startTime,DESC'}  # Adjust page size as needed
    while url:
        response = requests.get(url, auth=auth, params=params, verify=False)
        if response.status_code == 200:
            data = response.json()
            scans.extend(data['resources'])
            if 'page' in data and 'next' in data['page']:
                params['page'] += 1
            else:
                break
        else:
            print(f'Failed to retrieve scans: {response.status_code}')
            print(response.text)
            break
    return scans

# Make the request
scans = get_all_scans(url, (username, password))

# Debugging: Print all scans retrieved
print("All Scans Retrieved:")
for scan in scans[:30]:  # Limit to the most recent 30 scans
    scan_id = scan.get("id", "N/A")
    scan_name = scan.get("scanName", "N/A")
    scan_status = scan.get("status", "N/A")
    scan_start_time = scan.get("startTime", "N/A")
    scan_end_time = scan.get("endTime", "N/A")
    site_id = scan.get("siteId", "N/A")
    site_name = scan.get("siteName", "N/A")
    print(f'ID: {scan_id}, Name: {scan_name}, Status: {scan_status}, Start Time: {scan_start_time}, End Time: {scan_end_time}, Site Name: {site_name}')

running_scans = [scan for scan in scans if scan.get('status') == 'running']

if running_scans:
    print("Running Scans:")
    for scan in running_scans:
        scan_id = scan.get('id', 'N/A')
        scan_name = scan.get('scanName', 'N/A')
        scan_status = scan.get('status', 'N/A')
        scan_start_time = scan.get('startTime', 'N/A')
        scan_end_time = scan.get('endTime', 'N/A')
        site_id = scan.get("siteId", "N/A")
        site_name = scan.get("siteName", "N/A")
        print(f'ID: {scan_id}, Name: {scan_name}, Status: {scan_status}, Start Time: {scan_start_time}, End Time: {scan_end_time}, Site Name: {site_name}')
else:
    print("No running scans found.")

~~~