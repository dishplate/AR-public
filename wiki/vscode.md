# VSCode config on Mac

## Setup your VM with VMware Fusion, it's free on broadcom's website
https://github.com/dishplate/AR-public/blob/main/wiki/Vmware-fusion-on-Mac-(with-Apple-Silicon).md
## Install SSH server
    sudo apt update && sudo apt upgrade && sudo install openssh-server

## On Mac - allow VScode to access the local network
    Settings>Privacy & Security>Local Network and allow VS Code.

## Setup VScode for ssh access to the Linux VM
Test ssh access to the VM on Mac terminal first.
Click connect and select to remote host
Then configure SSH Hosts
Setup IP and Hostname - more than likely hostname won't work, use IP for both name and IP.
Click connect and some stuff will install
Clone a git repo and work!