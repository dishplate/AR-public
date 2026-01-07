# Netplan
Edit the network settings in 
~~~
/etc/netplan/some file name
The /etc/netplan/ directory can contain multiple .yaml config files.
~~~
### Use 
~~~
netplan try 
netplan apply
~~~
to test the settings or keep settings

## Example of netplan config file
~~~
network:
    version: 2
    renderer: networkd
    ethernets:
        enp3s0:
            addresses:
                - 10.10.10.2/24
            nameservers:
                search: [mydomain, otherdomain]
                addresses: [10.10.10.1, 1.1.1.1]
            routes:
                - to: default
                  via: 10.10.10.1
~~~
## Avoiding Common YAML Errors# 
All elements must be indented consistently using spaces (not tabs)
Netplan uses typed data for values. Be sure to wrap strings in quotes
You can also use numbers, booleans, nested objects, lists and other data types. Refer to the Netplan data types documentation for more details
Use 
~~~
netplan --debug apply
~~~
to enable verbose logging for troubleshooting.

