```
#remove_rfc1918_and_ipv6_addresses from another IP range

import csv

import ipaddress

def remove_rfc1918_and_ipv6_addresses(input_csv, output_csv):

    rfc1918_networks_v4 = [

        ipaddress.IPv4Network('[10.0.0.0/8'](http://10.0.0.0/8')),

        ipaddress.IPv4Network('[172.16.0.0/12'](http://172.16.0.0/12')),

        ipaddress.IPv4Network('[192.168.0.0/16](http://192.168.0.0/16)')

    ]

    cleaned_ips = []

    with open(input_csv, 'r') as infile:

        reader = csv.reader(infile)

        for row in reader:

            ip_str = row[0].strip()  # Assuming IP address is in the first column

            try:

                ip = ipaddress.IPv4Address(ip_str)

                if not any(ip in network for network in rfc1918_networks_v4):

                    cleaned_ips.append([ip_str])

            except ipaddress.AddressValueError:

                # Skip IPv6 addresses

                continue

    with open(output_csv, 'w', newline='') as outfile:

        writer = csv.writer(outfile)

        writer.writerows(cleaned_ips)


# Example usage:

input_csv = r'd:/experimental/ip_things/2024-04-04_All_ip-address-2-just-ips.csv'

output_csv = r'd:/experimental/ip_things/OUTPUT-2024-04-04_All_ip-address-2-just-ips.csv'

remove_rfc1918_and_ipv6_addresses(input_csv, output_csv)

print("IPv6 and RFC1918 addresses removed. Output saved to", output_csv)
+++++++++++++++++++++++++++++++++++++++++++++++++
IP EXPANDER

#2024-07-03 added option to expand CIDR ranges and a column with quotes and trailing comma

import csv

import ipaddress

from datetime import datetime

def expand_ip_ranges(ip_ranges):

    expanded_ips = []

    for ip_range in ip_ranges:

        if '-' in ip_range:

            start, end = ip_range.split(' - ')

            start_ip = ipaddress.ip_address(start.strip())

            end_ip = ipaddress.ip_address(end.strip())

            for ip_int in range(int(start_ip), int(end_ip) + 1):

                expanded_ips.append(str(ipaddress.ip_address(ip_int)))

        elif '/' in ip_range:

            network = ipaddress.ip_network(ip_range.strip(), strict=False)

            expanded_ips.extend([str(ip) for ip in network.hosts()])

        else:

            expanded_ips.append(ip_range.strip())

    return expanded_ips




# IP ranges in a single string

ip_ranges_str = ''192.168.1.1 - 192.168.1.200'''




ip_ranges = [ip.strip() for ip in ip_ranges_str.split(',')]




expanded_ips = expand_ip_ranges(ip_ranges)




# Get the current date and time

current_datetime = datetime.now()

folder = r'd:/'

file_name = r'Domain_controllers-expanded.csv'

file_name_with_date = str(folder) + "/" + str(current_datetime.strftime("%Y%m%d")) + "-" + str(file_name)

print(file_name_with_date)




# Write the expanded IP addresses to a CSV file

with open(file_name_with_date, 'w', newline='') as csvfile:

    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(['Expanded IP Addresses', 'Formatted IP Addresses'])

    for ip in expanded_ips:

        formatted_ip = f'"{ip}",'

        csv_writer.writerow([ip, formatted_ip])




print("Expanded IP addresses written to:", file_name_with_date)




++++++++++++++++++++++++++++++++++++++++++

Is range part of another IP range script

#2024-05-02 works.

#Fixed issue with duplicate number of ip addresses showing up in the matched ip column.

#Use this to find what ip addresses might be scanned by two sites

#Save the Nexpose site scan range in file 1 and file 2 for the other site.




import csv

import ipaddress

from openpyxl import Workbook

import os




# Define input file paths

input_file_1 = r'D:\experimental\LDN\internal_services_ip_range_2024-03-06.txt'

input_file_2 = r'D:\experimental\LDN\LDN-site-range.txt'

output_file = r'D:\experimental\LDN\compared_ip_addresses.xlsx'




def expand_ip_ranges(ip_ranges):

    expanded_ips = set()  # Use set to ensure uniqueness

    for ip_range in ip_ranges:

        if '-' in ip_range:  # If the IP range is specified as a range

            start_ip, end_ip = ip_range.split(' - ')

            start_ip = ipaddress.IPv4Address(start_ip.strip())

            end_ip = ipaddress.IPv4Address(end_ip.strip())

            # Manually generate all IP addresses in the range

            current_ip = start_ip

            while current_ip <= end_ip:

                expanded_ips.add(str(current_ip))

                current_ip += 1

        else:  # If single IP

            ip = ipaddress.IPv4Address(ip_range.strip())

            expanded_ips.add(str(ip))

    return expanded_ips




def count_ips_in_csv(csv_file):

    ip_ranges = []

    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:

        reader = csv.reader(csvfile)

        for row in reader:

            ip_ranges.extend(row)

    expanded_ips = expand_ip_ranges(ip_ranges)

    return expanded_ips




# Get expanded IP addresses from input files

input_ips_1 = count_ips_in_csv(input_file_1)

input_ips_2 = count_ips_in_csv(input_file_2)




# Find common IP addresses between input files

matched_ips = input_ips_1.intersection(input_ips_2)




# Write data to Excel file

wb = Workbook()

ws = wb.active




# Write headers

input_file_name_1 = os.path.basename(input_file_1)

input_file_name_2 = os.path.basename(input_file_2)

ws.append([f"Expanded IP Addresses from {input_file_name_1}", f"Expanded IP Addresses from {input_file_name_2}", "Matched IP Addresses"])




# Write expanded IP addresses from input file 1

for ip in input_ips_1:

    matched = ip in matched_ips

    ws.append([ip, None, None])




# Write expanded IP addresses from input file 2

for ip in input_ips_2:

    matched = ip in matched_ips

    ws.append([None, ip, None])




# Write matched IP addresses

for ip in matched_ips:

    ws.append([None, None, ip])




# Save the workbook to a file

wb.save(output_file)




print("\nScript's done!")




+++++++++++++++++++++++++++++++

#This works 2024-03-17

#This script will take an input csv with dashes and commas as obtained from Nexpose when editing a site.

#The exclusions csv follows the same format 172.16.1.1 - 172.16.1.100, 192.168.1.1, etc




import csv

import ipaddress

# Define input file path

input_file = r'd:/experimental/ip_ranges/internal_services_ip_range_2024-03-06.txt'


# exclusions_file = r'd:/experimental/ip_ranges/internal_services-exclusions_list_2024-03-14.txt'

exclusions_file = r'd:/experimental/ip_ranges/TOK_scanned_ip_ranges.txt'


output_file = r'd:/experimental/ip_ranges/TOK_exclusions_REMOVED_test.txt'


def expand_ip_ranges(ip_ranges):

    expanded_ips = set()  # Use set to ensure uniqueness

    for ip_range in ip_ranges:

        if '-' in ip_range:  # If the IP range is specified as a range

            start_ip, end_ip = ip_range.split(' - ')

            start_ip = ipaddress.IPv4Address(start_ip.strip())

            end_ip = ipaddress.IPv4Address(end_ip.strip())

            # Manually generate all IP addresses in the range

            current_ip = start_ip

            while current_ip <= end_ip:

                expanded_ips.add(str(current_ip))

                current_ip += 1

        else:  # If single IP

            ip = ipaddress.IPv4Address(ip_range.strip())

            expanded_ips.add(str(ip))

    return expanded_ips


def count_ips_in_csv(csv_file):

    ip_ranges = []

    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:

        reader = csv.reader(csvfile)

        for row in reader:

            ip_ranges.extend(row)

    expanded_ips = expand_ip_ranges(ip_ranges)

    return expanded_ips


# Get IP addresses from input file

input_ips = count_ips_in_csv(input_file)


# Get IP addresses from exclusions file

exclusions_ips = count_ips_in_csv(exclusions_file)


# Remove IP addresses from exclusions file from IP addresses in input file

cleaned_ips = input_ips - exclusions_ips

# Count the total number of cleaned IP addresses

cleaned_ips_count = len(cleaned_ips)


# Count the total number of IP addresses in the input file

input_ips_count = len(input_ips)

# Count the total number of IP addresses in the exclusions file

exclusions_ips_count = len(exclusions_ips)


# Print number of IP addresses in input file

print("Number of IP addresses in input file:", input_ips_count)

# Print number of IP addresses in exclusions file

print("Number of IP addresses in exclusions file:", exclusions_ips_count)

# Print number of cleaned IP addresses

print("Number of cleaned IP addresses:", cleaned_ips_count)
```