```
#10/24/24 This works
import csv
from tenable.nessus import Nessus

# Variables to customize
NESSUS_URL = 'https://172.22.22.103:8834'  # URL of your Nessus server
ACCESS_KEY = 'xxx'                  # Your Nessus access key
SECRET_KEY = 'xxx'                  # Your Nessus secret key
SCAN_ID = 8                                     # The scan ID you want to export
OUTPUT_FILE = '/home/nessus_output/vulnerabilities.csv'             # The name of the CSV file to export the data to

# Initialize Nessus connection using access key and secret key
nessus = Nessus(
    url=NESSUS_URL,
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY
)

# Function to fetch and export scan results to a CSV file
def export_vuln_data_to_csv(scan_id, output_file=OUTPUT_FILE):
    # Fetch scan details using the scan ID
    scan_details = nessus.scans.details(scan_id)

    # Prepare the CSV file for writing
    with open(output_file, mode='w', newline='') as csv_file:
        fieldnames = ['IP Address', 'Hostname', 'CVE', 'Severity', 'Date Found', 'OS Name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Iterate through each host in the scan details
        for host in scan_details['hosts']:
            ip_address = host['hostname']  # IP address
            hostname = host.get('netbios_name', 'N/A')  # Hostname or fallback to 'N/A'
            os_name = host.get('operating_system', 'N/A')  # OS Name or fallback to 'N/A'

            # Check if the 'vulnerabilities' key exists
            if 'vulnerabilities' in host:
                # Fetch vulnerabilities for each host
                for vuln in host['vulnerabilities']:
                    cve = vuln['cve'][0] if vuln.get('cve') else 'N/A'  # Get the first CVE or 'N/A'
                    severity = vuln['severity']  # Severity level
                    date_found = vuln['plugin_publication_date']  # Date the vulnerability was found

                    # Write the row with the details
                    writer.writerow({
                        'IP Address': ip_address,
                        'Hostname': hostname,
                        'CVE': cve,
                        'Severity': severity,
                        'Date Found': date_found,
                        'OS Name': os_name
                    })
            else:
                # Optionally, you can handle hosts without vulnerabilities here
                print(f"No vulnerabilities found for {hostname} ({ip_address})")

    print(f"Vulnerability data exported to {output_file}")

# Export the vulnerability data for the specified scan to CSV
export_vuln_data_to_csv(SCAN_ID)
```