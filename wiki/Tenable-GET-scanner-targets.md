~~~
import requests

# === CONFIGURATION ===
ACCESS_KEY = 'YOUR_ACCESS_KEY'
SECRET_KEY = 'YOUR_SECRET_KEY'
SCANNER_NAME = 'YOUR_SCANNER_NAME'  # e.g., 'Internal Scanner 1'

BASE_URL = 'https://cloud.tenable.com'
HEADERS = {
    'X-ApiKeys': f'accessKey={ACCESS_KEY}; secretKey={SECRET_KEY}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# === GET SCANNERS ===
def get_scanner_id(scanner_name):
    response = requests.get(f'{BASE_URL}/scanners', headers=HEADERS)
    response.raise_for_status()
    for scanner in response.json()['scanners']:
        if scanner['name'].lower() == scanner_name.lower():
            return scanner['id']
    return None

# === GET SCANS FOR THAT SCANNER ===
def get_scans_for_scanner(scanner_id):
    response = requests.get(f'{BASE_URL}/scans', headers=HEADERS)
    response.raise_for_status()
    scans = response.json().get('scans', [])
    return [scan for scan in scans if scan.get('scanner_id') == scanner_id]

# === GET TARGETS FROM EACH SCAN ===
def get_targets(scan_id):
    response = requests.get(f'{BASE_URL}/scans/{scan_id}', headers=HEADERS)
    response.raise_for_status()
    return response.json()['info'].get('targets', '')

# === MAIN ===
def main():
    scanner_id = get_scanner_id(SCANNER_NAME)
    if not scanner_id:
        print(f"Scanner '{SCANNER_NAME}' not found.")
        return

    scans = get_scans_for_scanner(scanner_id)
    print(f"\nFound {len(scans)} scans for scanner '{SCANNER_NAME}':\n")

    for scan in scans:
        scan_id = scan['id']
        scan_name = scan['name']
        targets = get_targets(scan_id)
        print(f"- Scan: {scan_name} (ID: {scan_id})")
        print(f"  Targets: {targets}\n")

if __name__ == '__main__':
    main()

~~~