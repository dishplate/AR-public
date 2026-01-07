# Linux Static ip & root login
~~~
Open cloud-init file “/etc/cloud/cloud.cfg.d/subiquity-disable-cloudinit-networking.cfg” and make sure entry “network: {config: disabled}” is there. In case this entry is missing, then add it manually. 
 
edit the netplan configuration file “/etc/netplan/00-installer-config.yaml”. 
Two spaces separate the levels in this yml file. Eg. Ethernets is two spaces further from the margin than network. 
$ sudo vi /etc/netplan/00-installer-config.yaml 
# This is the network config written by 'subiquity' 
network: 
  ethernets: 
    enp0s3: 
      dhcp4: true 
  version: 2 
 
 
STATIC CONFIG 
$ sudo vi /etc/netplan/00-installer-config.yaml 
# This is the network config written by 'subiquity' 
network: 
  renderer: networkd 
  ethernets: 
    ens18: 
      addresses: 
        - 10.1.1.250/24 
      nameservers: 
        addresses: [10.1.1.150, 10.1.1.6] 
      routes: 
        - to: default 
          via: 10.1.1.1 
  version: 2 
 
 
Run the following “netplan apply” command to make the above changes into the effect. 
 
In case you run into some issues execute: 
sudo netplan --debug apply 
+++++++++++++++++++++ 
 
Allowing root login. 
 
Nano /etc/ssh/sshd_config 
Edit the  line with PermitRootLogin to 
PermitRootLogin yes 
 
Restart ssh service 
Sudo systemctl restart ssh 
 
FOR DEBIAN 
FROM: 
PermitRootLogin without-password 
 
TO: 
PermitRootLogin yes 
~~~