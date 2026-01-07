~~~

from tenable.io import TenableIO

# Replace with your Tenable.io API keys
ACCESS_KEY = "your_access_key"
SECRET_KEY = "your_secret_key"

# Initialize Tenable.io connection
tio = TenableIO(ACCESS_KEY, SECRET_KEY)

# Retrieve scans
scans = tio.scans.list()

# Filter running scans
running_scans = [scan for scan in scans if scan['status'] == 'running']

# Print running scans
for scan in running_scans:
    print(f"Scan ID: {scan['id']}, Name: {scan['name']}, Status: {scan['status']}")

~~~