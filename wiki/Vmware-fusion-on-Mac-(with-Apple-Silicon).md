# Vmware fusion with the following setup:
* Macs with Apple silicon
* Linux guest OS
don't use the the normal process to install vmware tools.
You must install Open VM Tools
https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-1-0/vmware-tools-administration-12-1-0/introduction-to-vmware-tools/open-vm-tools.html

## Broadcom docs lead you in circles, you can build these from vmware's github repo or install from your distro's package manager:
1. apt install open-vm-tools
1. apt install open-vm-tools-desktop