```
// List of hostnames to include; remove or comment out to include all systems
// let hostnames = datatable (hostname: string)
// ["blah.global",
// ];
DeviceTvmSoftwareVulnerabilities
// | where DeviceName in (hostnames)
| where SoftwareVendor contains "microsoft"
| where OSPlatform !contains "macOS"
| where OSPlatform !contains "server"
| join kind=inner (
    DeviceTvmSoftwareVulnerabilitiesKB
    // Ensure there is a `PublishedDate` field and adjust the field name if necessary
    | where AffectedSoftware contains "microsoft"
    | where PublishedDate <= datetime(2024-06-11)
    | project CveId, CvssScore, PublishedDate
) on CveId
| extend CriticalVuln = iif(CvssScore >= 7.5 and CvssScore <= 10, 1, 0)
| extend SevereVuln = iif(CvssScore >= 3.5 and CvssScore < 7.5, 1, 0)
| extend ModerateVuln = iif(CvssScore >=0 and CvssScore < 3.5, 1, 0)
// Remove the lines below to view all systems and all vulns
// | summarize CriticalVulns = sum(CriticalVuln), SevereVulns = sum(SevereVuln), ModerateVulns = sum(ModerateVuln) by DeviceName, DeviceId, OSPlatform
// | order by CriticalVulns desc//, SevereVulns desc
| top 30 by CriticalVuln
```