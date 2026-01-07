```
// Store the list of DeviceNames in a variable where the device is onboarded
let deviceNames = DeviceInfo
                  | where Onboarded == true
                  | distinct DeviceName;

// Use the variable in another query
DeviceTvmSoftwareVulnerabilities
| where DeviceName in (deviceNames)
| project DeviceName, SoftwareName, CveId, Severity
```
