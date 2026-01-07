~~~
import requests
from requests.auth import HTTPBasicAuth
from collections import Counter

# Credentials
username = '<YOUR_USERNAME>'
password = '<YOUR_PASSWORD>'
console_url = '<YOUR_CONSOLE_URL>'

# List of site IDs to exclude
excluded_sites = {101: 'Test Site A', 202: 'Maintenance Site B'}  # Replace with your site IDs and names

# API endpoint for scan engines
url = f'{console_url}/api/3/scan_engines'

# Make the request
response = requests.get(url, auth=HTTPBasicAuth(username, password))
excluded_log = []
version_counter = Counter()  # To track engine versions
inactive_engines = []  # To track engines with non-active status

if response.status_code == 200:
    engines = response.json()['resources']
    for engine in engines:
        engine_id = engine['id']
        engine_name = engine['name']
        engine_version = engine.get('version', 'N/A')
        site_id = engine.get('siteId')  # Assuming 'siteId' is part of the engine response
        engine_status = engine.get('status', 'N/A').lower()  # Ensure comparison is case-insensitive
        
        # Skip engines belonging to excluded sites
        if site_id in excluded_sites:
            excluded_log.append(f'Skipped: Engine ID {engine_id} (Site ID {site_id}: {excluded_sites[site_id]})')
            continue
        
        # Check for non-active engines
        if engine_status != 'active':
            inactive_engines.append(f'Engine ID {engine_id}, Name: {engine_name}, Status: {engine_status.capitalize()}')
        
        # Print engine details and update version counter
        print(f'ID: {engine_id}, Name: {engine_name}, Version: {engine_version}')
        version_counter[engine_version] += 1
    
    # Log excluded sites at the end
    print("\nExcluded Engines:")
    for log_entry in excluded_log:
        print(log_entry)
    
    # Summary of engine versions
    print("\nEngine Version Summary:")
    for version, count in version_counter.items():
        print(f'Version {version}: {count} engine(s)')
    
    # Print details of non-active engines
    if inactive_engines:
        print("\nNon-Active Engines:")
        for engine_info in inactive_engines:
            print(engine_info)
else:
    print(f'Failed to retrieve engines: {response.status_code}')
    print(response.text)

~~~