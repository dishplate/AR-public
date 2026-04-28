```
DeviceTvmSoftwareInventory
| where EndOfSupportStatus == 'EOS Version'
| where SoftwareName == 'linux'
| where OSPlatform contains "Linux"
| where isnotempty(EndOfSupportStatus)
| join kind=inner (DeviceInfo | project DeviceId, DeviceName, IPAddress) on DeviceId
| project DeviceName, IPAddress, SoftwareName, EndOfSupportStatus, OSPlatform
```