~~~
Untested 
Resources
| where type == "microsoft.compute/virtualmachines"
| extend vmId = tostring(properties.vmId), nicIds = properties.networkProfile.networkInterfaces
| mv-expand nic = nicIds
| extend nicId = tostring(nic.id)
| join kind=leftouter (
    Resources
    | where type == "microsoft.network/networkinterfaces"
    | extend nicId = tolower(id), ipConfigs = properties.ipConfigurations
    | mv-expand ipConfig = ipConfigs
    | extend privateIp = tostring(ipConfig.properties.privateIPAddress)
    | project nicId, privateIp
) on $left.nicId == $right.nicId
| project subscriptionId, resourceGroup, vmName = name, location, privateIp



Another one

Resources
| where type == "microsoft.compute/virtualmachines"
| extend vmId = tostring(properties.vmId),
         osType = tostring(properties.storageProfile.osDisk.osType),
         publisher = tostring(properties.storageProfile.imageReference.publisher),
         offer = tostring(properties.storageProfile.imageReference.offer),
         sku = tostring(properties.storageProfile.imageReference.sku),
         nicIds = properties.networkProfile.networkInterfaces
| mv-expand nic = nicIds
| extend nicId = tostring(nic.id)
| join kind=leftouter (
    Resources
    | where type == "microsoft.network/networkinterfaces"
    | extend nicId = tolower(id), ipConfigs = properties.ipConfigurations
    | mv-expand ipConfig = ipConfigs
    | extend privateIp = tostring(ipConfig.properties.privateIPAddress)
    | project nicId, privateIp
) on $left.nicId == $right.nicId
| project subscriptionId, resourceGroup, vmName = name, location, osType, publisher, offer, sku, privateIp


Another test to fix missing IP addresses

Resources
| where type == "microsoft.compute/virtualmachines"
| extend vmId = tostring(properties.vmId),
         osType = tostring(properties.storageProfile.osDisk.osType),
         publisher = tostring(properties.storageProfile.imageReference.publisher),
         offer = tostring(properties.storageProfile.imageReference.offer),
         sku = tostring(properties.storageProfile.imageReference.sku),
         nicIds = properties.networkProfile.networkInterfaces
| mv-expand nic = nicIds
| extend nicId = tolower(tostring(nic.id))  // force lowercase for join
| join kind=leftouter (
    Resources
    | where type == "microsoft.network/networkinterfaces"
    | extend nicId = tolower(id), ipConfigs = properties.ipConfigurations
    | mv-expand ipConfig = ipConfigs
    | extend privateIp = tostring(ipConfig.properties.privateIPAddress)
    | project nicId, privateIp
) on $left.nicId == $right.nicId
| project subscriptionId, resourceGroup, vmName = name, location, osType, publisher, offer, sku, privateIp



another to include public ip


Resources
| where type == "microsoft.compute/virtualmachines"
| extend vmId = tostring(properties.vmId),
         osType = tostring(properties.storageProfile.osDisk.osType),
         publisher = tostring(properties.storageProfile.imageReference.publisher),
         offer = tostring(properties.storageProfile.imageReference.offer),
         sku = tostring(properties.storageProfile.imageReference.sku),
         nicIds = properties.networkProfile.networkInterfaces
| mv-expand nic = nicIds
| extend nicId = tolower(tostring(nic.id))
| join kind=leftouter (
    Resources
    | where type == "microsoft.network/networkinterfaces"
    | extend nicId = tolower(id), ipConfigs = properties.ipConfigurations
    | mv-expand ipConfig = ipConfigs
    | extend privateIp = tostring(ipConfig.properties.privateIPAddress),
             publicIpId = tostring(ipConfig.properties.publicIPAddress.id)
    | join kind=leftouter (
        Resources
        | where type == "microsoft.network/publicipaddresses"
        | project publicIpId = tolower(id), publicIp = tostring(properties.ipAddress)
    ) on publicIpId
    | project nicId, privateIp, publicIp
) on $left.nicId == $right.nicId
| project subscriptionId, resourceGroup, vmName = name, location, osType, publisher, offer, sku, privateIp, publicIp


Another to fix public IP not working

// Step 1: Get VM info and NIC IDs
Resources
| where type == "microsoft.compute/virtualmachines"
| extend vmId = tostring(properties.vmId),
         osType = tostring(properties.storageProfile.osDisk.osType),
         publisher = tostring(properties.storageProfile.imageReference.publisher),
         offer = tostring(properties.storageProfile.imageReference.offer),
         sku = tostring(properties.storageProfile.imageReference.sku),
         nicIds = properties.networkProfile.networkInterfaces
| mv-expand nic = nicIds
| extend nicId = tolower(tostring(nic.id))
| join kind=leftouter (
// Step 2: Get NICs and IP configs
    Resources
    | where type == "microsoft.network/networkinterfaces"
    | extend nicId = tolower(id),
             ipConfigs = properties.ipConfigurations
    | mv-expand ipConfig = ipConfigs
    | extend privateIp = tostring(ipConfig.properties.privateIPAddress),
             publicIpRef = tostring(ipConfig.properties.publicIPAddress.id),
             ipConfigName = tostring(ipConfig.name)
    | project nicId, privateIp, publicIpRef, ipConfigName
) on $left.nicId == $right.nicId
| extend publicIpId = tolower(publicIpRef)
| join kind=leftouter (
// Step 3: Get Public IPs
    Resources
    | where type == "microsoft.network/publicipaddresses"
    | extend publicIpId = tolower(id),
             publicIp = tostring(properties.ipAddress)
    | project publicIpId, publicIp
) on publicIpId
| project subscriptionId, resourceGroup, vmName = name, location,
          osType, publisher, offer, sku,
          privateIp, publicIp

~~~