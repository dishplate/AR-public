```
 Windows Servers asset totals
DeviceInfo
//Remember to choose 30 days for reporting
//Windows server asset count query
| where OSPlatform contains "server"
| where OSPlatform contains "Windows"
| where OnboardingStatus == "Onboarded"
| where Timestamp >= ago(30d)
| summarize make_set(DeviceName) by OSPlatform, DeviceName, DeviceManualTags, DeviceDynamicTags
//use distinct to avoid having to dedupe
| distinct DeviceName

Windows Workstations
DeviceInfo
//Windows workstation asset count query
| where OSPlatform contains "Windows"
| where OSPlatform !contains "server"
| where OnboardingStatus == "Onboarded"
| where Timestamp >= ago(30d)
| summarize make_set(DeviceName) by OSPlatform, DeviceName, DeviceManualTags, DeviceDynamicTags
//use distinct to avoid having to dedupe
| distinct DeviceName

Linux
DeviceInfo
| where OSPlatform contains "linux" and OnboardingStatus == "Onboarded"
| where Timestamp >= ago(30d)
| summarize make_set(DeviceName) by OSPlatform, DeviceName, DeviceManualTags, DeviceDynamicTags, OnboardingStatus
//use distinct to avoid having to dedupe
| distinct DeviceName

MacOS
DeviceInfo
//Export to excel sort for EOL versions 
//https://support-en.wd.com/app/answers/detailweb/a_id/50816/~/apple-macos-end-of-support
| where OSPlatform == "macOS" and OnboardingStatus =="Onboarded" 
| where Timestamp >= ago(30d)
| summarize by DeviceName, DeviceId, OSDistribution, Model, DeviceType, OnboardingStatus, Timestamp
| summarize LastScanTime=max(Timestamp) by DeviceId, DeviceName
// | distinct DeviceName, Timestamp

EOL
Windows Servers
DeviceTvmSoftwareInventory
// EXPORT and separate the servers from workstations
| where EndOfSupportStatus != "" and OSPlatform contains "Windows" 
//| where Timestamp >= ago(30d) Timestamp doesn't work without the deviceinfo table
| where SoftwareVendor contains "Microsoft" 
| where  SoftwareName contains "server"
| where  SoftwareName contains "windows"
| project DeviceId, DeviceName, EndOfSupportStatus, SoftwareName, SoftwareVendor, SoftwareVersion, OSPlatform, OSVersion
//use distinct to avoid having to dedupe
| distinct DeviceName

Windows Workstations
DeviceTvmSoftwareInventory
// EXPORT and separate the servers from workstations
| where EndOfSupportStatus != "" and OSPlatform contains "Windows" 
//| where Timestamp >= ago(30d) Timestamp doesn't work without the deviceinfo table
| where SoftwareVendor contains "Microsoft" 
| where  SoftwareName !contains "server"
| where  SoftwareName contains "windows"
| project DeviceId, DeviceName, EndOfSupportStatus, SoftwareName, SoftwareVendor, SoftwareVersion, OSPlatform, OSVersion
//use distinct to avoid having to dedupe
| distinct DeviceName

MAC
DeviceInfo
//EOL as defind in here https://support-en.wd.com/app/answers/detailweb/a_id/50816/~/apple-macos-end-of-support
| where Timestamp >= ago(30d)
| where OSPlatform == "macOS" and OnboardingStatus =="Onboarded" 
| where toreal(OSVersion) <= 12
| summarize by DeviceName, OSVersionInfo, OSVersion, DeviceType, OnboardingStatus

Linux
Use the GUI. Assets > filter for Linux and onboarded.
Export to Excel and filter for OS versions, pick the EOL systems.
Top 25 Riskiest Workstations, can be modified for servers etc.
// List of builders to include; remove or comment out to include all systems 
// Update the PublishedDate to the date of the last patch Tuesday 
// list below removes builders let builders = datatable (hostname: string)
["computer",];
DeviceTvmSoftwareVulnerabilities
// | where DeviceName contains "system"
| where DeviceName !in (builders)
//Exclusions
| where DeviceName != "computer01" //Exclusions here
| where OSArchitecture !contains "unknown"
| where SoftwareVendor contains "microsoft"
| where OSPlatform !contains "macOS"
| where OSPlatform !contains "server"
| join kind=inner (
DeviceTvmSoftwareVulnerabilitiesKB
| where AffectedSoftware contains "microsoft"
| project CveId, CvssScore, PublishedDate//, IsExploitAvailable
) on CveId
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

Site report template
// template for site reports by IP address
let IpList = datatable(IPAddress:string)
["192.168.1.1"];
let extractedIPs = DeviceNetworkInfo
| mv-expand IPObject = parse_json(IPAddresses)  // Expand JSON array into individual objects
| extend IP = tostring(IPObject.IPAddress)  // Extract IP address
| where IP in (IpList)
| summarize by DeviceId, DeviceName;
extractedIPs
| join kind=inner (DeviceTvmSoftwareVulnerabilities) on $left.DeviceId == $right.DeviceId
| where SoftwareVendor contains "Microsoft"
// | project DeviceName, SoftwareName, SoftwareVendor, VulnerabilitySeverityLevel
| limit 100 


Get list of CVEs on a device
DeviceTvmSoftwareVulnerabilities
| where DeviceName == "computerNAME.global"
| join kind=inner DeviceTvmSoftwareVulnerabilitiesKB on $left.CveId == $right.CveId
| project DeviceName, CveId, AffectedSoftware, PublishedDate, IsExploitAvailable, VulnerabilityDescription, CvssScore, LastModifiedTime, VulnerabilitySeverityLevel
Find a CVE
DeviceTvmSoftwareVulnerabilities
| where CveId == "CVE-2024-30080"
| join kind=inner (
    DeviceNetworkInfo
    | summarize arg_max(Timestamp, *) by DeviceId
) on DeviceId
| project DeviceName, IPAddresses, CveId, SoftwareName, SoftwareVendor, SoftwareVersion
List only Microsoft CVE's (or other software vendor)
Watch the 'contains' option for short system names that may have more than one return
DeviceTvmSoftwareVulnerabilities
| where SoftwareVendor contains "Microsoft"
| where DeviceName contains "Computer.global"
| project CveId, DeviceName

Finding installed software
DeviceTvmSoftwareInventory
| where SoftwareVendor contains "VMware"
| project DeviceName, SoftwareName
Wi-Fi connected devices in the last day that are up
DeviceNetworkInfo
| where NetworkAdapterType contains "wireless"
and NetworkAdapterStatus contains "up"
| where isnotempty( ConnectedNetworks)
| where Timestamp > ago(1d)
| summarize any(DeviceName,NetworkAdapterType, NetworkAdapterStatus, NetworkAdapterVendor, ConnectedNetworks, Timestamp) by DeviceName
regreSSHion vulnerability
DeviceTvmSoftwareVulnerabilities
| where CveId == "CVE-2024-6387" or CveId == "CVE-2006-5051"
| join kind=inner (
    DeviceNetworkInfo
    | summarize arg_max(Timestamp, *) by DeviceId
) on DeviceId
| mv-expand IPObject = parse_json(IPAddresses)  // Expand JSON array into individual objects
| extend IP = tostring(IPObject.IPAddress)  // Extract IP address
// | where OSPlatform contains "Linux"
| project DeviceName, IP,IPAddresses,OSPlatform, CveId, SoftwareName, SoftwareVendor, SoftwareVersion, NetworkAdapterVendor,Timestamp
| distinct DeviceName, OSPlatform, IP, Timestamp, SoftwareName, SoftwareVendor, CveId
// enable the line below to remove xbox systems
| where DeviceName !contains "xb"
```