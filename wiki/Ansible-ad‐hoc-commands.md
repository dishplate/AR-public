# Ansible ad-hoc commands
~~~
Using adhoc commands with a host/inventory file
Ping ALL of your nodes defined in your ansible inventory
Test it, ping all your hosts[nodes]
#ansible all -m ping
Change all to a host name AS DEFINED in your ansible inventory

If you ansible inventory lists a server as wazuh_server:
ansible wazuh_server -a "uname -a"

Get hostnames
$ansible all -a "hostname"

Free disk space
$ansible all -a “df -h”

# Basic syntax structure
$ ansible <group> -m <module> -a <arguments>

## Running a command 
--ask-become-pass
Eg. ansible nas -m apt -a 'upgrade=yes update_cache=yes' -b 

## Rebooting hosts
$ ansible <group> -a “/sbin/reboot”

## Shutting down a system
Ansible <group> -a "/sbin/shutdown -r now"

## Checking host’s system information
Ansible collects the system’s information for all the hosts connected to it. To display the information of hosts, run

$ ansible <group> -m setup | less

Secondly, to check a particular info from the collected information by passing an argument,

$ ansible <group> -m setup -a “filter=ansible_distribution”

~~~