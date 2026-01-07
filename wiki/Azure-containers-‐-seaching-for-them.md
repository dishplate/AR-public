~~~
Option 1: Azure Resource Graph (ARG)
Resources
| where type in~ ('microsoft.containerservice/managedclusters', 'microsoft.containerinstance/containergroups')
| project name, type, location, resourceGroup

Option 2: Log Analytics / Azure Monitor (if logs are enabled)
If AKS is sending logs to a Log Analytics workspace, you can query:

KubePodInventory
| project TimeGenerated, ClusterName, Namespace, PodName, ContainerName, Node

For ACI (if diagnostic logs are enabled):
ContainerInstanceLog_CL
| project TimeGenerated, ContainerGroup_s, ContainerName_s, Message_s

~~~