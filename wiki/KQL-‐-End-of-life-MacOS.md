```
DeviceInfo
| where Timestamp >= ago(30d)
| where OSPlatform == "macOS" and OnboardingStatus == "Onboarded"
| summarize by DeviceName, OSVersion
| extend IsEOL = iif(toreal(OSVersion) <= 12, "EOL", "Non-EOL")
| summarize Count = count() by IsEOL
| extend Label = strcat(IsEOL, ": ", tostring(Count))
| project Label, Count
| render piechart with(title="macOS Versions: EOL vs Non-EOL", legend=false)
```