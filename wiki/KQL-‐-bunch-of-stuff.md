```
Sometimes you have to remove and reenter your query to get a different result - it can get confused if you delete or comment out things, giving you differing output for the same query.


Workstations sorted by number of critical vulns

DeviceTvmSoftwareVulnerabilities
| where SoftwareVendor contains "Microsoft"
| where OSPlatform !contains "Server"
|where OSPlatform !contains "macOS"
| where VulnerabilitySeverityLevel in ('Critical', 'High', 'Medium', 'Low')
| summarize CriticalVulns = countif(VulnerabilitySeverityLevel == 'Critical'),
            HighVulns = countif(VulnerabilitySeverityLevel == 'High'),
            MediumVulns = countif(VulnerabilitySeverityLevel == 'Medium'),
            LowVulns = countif(VulnerabilitySeverityLevel == 'Low')
    by DeviceName, OSPlatform, OSArchitecture, OSVersion
| project DeviceName, CriticalVulns, HighVulns, MediumVulns, LowVulns, OSArchitecture, OSPlatform, OSVersion 
| sort by CriticalVulns
                                        

Quick summary of a table by OS platforms

DeviceTvmSoftwareInventory
| summarize by OSPlatform

Get a list of columns in a table
TABLE_NAME
| getschema



Setting up a list 
let hostnames = datatable (hostname: string)
[
    "computer.local",
    ];
DeviceInfo
| where DeviceName in (hostnames)
| sort by DeviceName
| limit 10
| project DeviceName, DeviceType, OSVersionInfo, OSBuild, OSPlatform

Lists from Nexpose to KQL
Take a csv output from Nexpose query builder and open in excel. Add quotes and commas that are needed in a KQL list, make a new column in excel and copy this down the column to add quotes and a trailing comma. Copy the list into the KQL query.
=CHAR(34) & B2 & CHAR(34) & CHAR(44) 

Lists - showing vulns in a site
let hostnames = datatable (hostname: string)
[
    "computer.global",
"icomputer1i.global",
];
DeviceTvmSoftwareVulnerabilities
| where DeviceName in (hostnames)
| where SoftwareVendor contains "Microsoft"
// | where OSPlatform !contains "Server"
|where OSPlatform !contains "macOS"
| where VulnerabilitySeverityLevel in ('Critical', 'High', 'Medium', 'Low')
| summarize CriticalVulns = countif(VulnerabilitySeverityLevel == 'Critical'),
            HighVulns = countif(VulnerabilitySeverityLevel == 'High'),
            MediumVulns = countif(VulnerabilitySeverityLevel == 'Medium'),
            LowVulns = countif(VulnerabilitySeverityLevel == 'Low')
    by DeviceName, OSPlatform, OSArchitecture, OSVersion
| project DeviceName, CriticalVulns, HighVulns, MediumVulns, LowVulns, OSArchitecture, OSPlatform, OSVersion 
| sort by CriticalVulns


Get list of CVEs on a device and link to KB table, use 'contains' if zero items are returned
DeviceTvmSoftwareVulnerabilities
| where DeviceName == "computerNAME.global"
| join kind=inner DeviceTvmSoftwareVulnerabilitiesKB on $left.CveId == $right.CveId
| project DeviceName, CveId, AffectedSoftware, PublishedDate, IsExploitAvailable, VulnerabilityDescription, CvssScore, LastModifiedTime, VulnerabilitySeverityLevel

List only Microsoft CVE's (or other software vendor)
Watch the 'contains' option for short system names that may have more than one return
DeviceTvmSoftwareVulnerabilities
| where SoftwareVendor contains "Microsoft"
| where DeviceName contains "computer.global"
| project CveId, DeviceName

Find installed software
DeviceTvmSoftwareInventory
| where SoftwareVendor contains "VMware"
| project DeviceName, SoftwareName


Span two tables (From kc7cyber ctf)
let mary_ips = 
Employees
| where name has "mary"
| distinct ip_addr;
OutboundNetworkEvents
| where src_ip in (mary_ips)
| count 

Span two tables - Kc7cyber example 2
let auth_attempts = Employees
| where name has "mary"
| distinct username;
AuthenticationEvents
| where username in (auth_attempts)
| count

Wi-Fi connected devices in the last day that are up
DeviceNetworkInfo 
| where NetworkAdapterType contains "wireless" 
and NetworkAdapterStatus contains "up"
| where isnotempty( ConnectedNetworks)
| where Timestamp > ago(1d)
| summarize any(DeviceName,NetworkAdapterType, NetworkAdapterStatus, NetworkAdapterVendor, ConnectedNetworks, Timestamp) by DeviceName

Wi-Fi devices with a specific vulnerability
DeviceNetworkInfo
| where NetworkAdapterType contains "wireless" 
and NetworkAdapterStatus contains "up"
| where isnotempty( ConnectedNetworks)
| where Timestamp > ago(1d)
| summarize any(DeviceName,NetworkAdapterType, NetworkAdapterStatus, NetworkAdapterVendor, ConnectedNetworks, Timestamp) by DeviceName
| join kind=innerunique DeviceTvmSoftwareVulnerabilities on DeviceName
| summarize by DeviceName, CveId, any_Timestamp, any_NetworkAdapterStatus, any_ConnectedNetworks
| where CveId contains "CVE-2024-30078"

Using a timestamp
where timestamp between (datetime(2024-01-01) .. datetime(2024-01-02))

Summarizing by OSPlatform or similar

DeviceTvmSoftwareInventory
| where SoftwareName has "TeamViewer"
| summarize Count = count() by OSPlatform
| order by Count desc

Filter for columns that are not empty
DeviceTvmSoftwareInventory
| where isnotempty(EndOfSupportStatus)

 [https://owl-records.com/account/security-questions?question_1=mother's+maiden+name&answer_1=Washington&question_2=first+pet's+name&answer_2=Fluffy](https://owl-records.com/account/security-questions?question_1=mother%27s+maiden+name&answer_1=Washington&question_2=first+pet%27s+name&answer_2=Fluffy),
"status_code": 200


Employees
| where role == "CEO"

InboundNetworkEvents
| where timestamp between (datetime("2024-04-10T00:00:00") .. datetime("2024-04-11T00:00:00"))
| where src_ip has "18.66.52.227"

InboundNetworkEvents
| where timestamp between (datetime("2024-04-10T00:00:00") .. datetime("2024-04-11T00:00:00"))
| where url has_any("washington", "fluffy")
| where src_ip has "18.66.52.227"

PassiveDns
| where ip == "18.66.52.227"
```