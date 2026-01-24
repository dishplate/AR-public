# VSCode config on Mac

## Setup your VM with VMware Fusion, it's free on broadcom's website
    See: https://github.com/dishplate/AR-public/blob/main/wiki/Vmware-fusion-on-Mac-(with-Apple-Silicon).md
## Install SSH server
    sudo apt update && sudo apt upgrade && sudo install openssh-server

## On Mac - allow VScode to access the local network
    Settings>Privacy & Security>Local Network and allow VS Code.

## Setup VScode for ssh access to the Linux VM
    1. Test ssh access to the VM on Mac terminal first