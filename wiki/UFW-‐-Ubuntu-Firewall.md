```
UFW Firewall 

UFW Firewall rules 
https://www.cherryservers.com/blog/how-to-configure-ubuntu-firewall-with-ufw 
https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04 
For DFW console 
Block all outgoing and incoming 
Allow incoming any ssh  
Allow incoming IT VLAN [10.16.11.0/24](http://10.16.11.0/24) to port 3780 
  
  
What was run 
 ufw allow ssh 
 ufw default deny incoming 
ufw default allow outgoing 
 ufw status verbose 
ufw allow from [10.16.11.0/24](http://10.16.11.0/24) to any port 3780 
 ufw logging medium (TURN THIS OFF - THIS SHOWS BLOCKED AND ALLOWED) 
  
Tested connectivity with ufw disabled then enabled and after a reboot 
 nc -vz [google.com](http://google.com/) 443 
 nc -vz [updates.rapid7.com](http://updates.rapid7.com/) 443 
 nc -zv 8.8.8.8 53 
  
root@dfw-nxpcon01:~# ufw status verbose 
Status: active 
Logging: on (medium) 
Default: deny (incoming), deny (outgoing), disabled (routed) 
New profiles: skip 
  
To                         Action      From 
--                         ------      ---- 
22                         ALLOW IN    Anywhere 
22/tcp                     ALLOW IN    Anywhere 
3780                       ALLOW IN    [10.16.11.0/24](http://10.16.11.0/24) 
22 (v6)                    ALLOW IN    Anywhere (v6) 
22/tcp (v6)                ALLOW IN    Anywhere (v6) 
  
root@dfw-nxpcon01:~# 
  
  
UFW DEFAULTS 
sudo ufw default deny incoming 
sudo ufw default allow outgoing 
  
Don't lock yourself out of SSH access to the server. 
 ufw allow ssh gets the definition (port) of ssh from /etc/services which is usually port 22 
 ufw allow 22 is a safe bet for port ssh. 
  
 ufw show added will show you your rules even if the firewall is not enabled. 
  
ufw status numbered 
 ufw status verbose shows you your defaults 
  
Rules can be found here too: 
 cat /etc/ufw/user.rules 
  
Cheatsheet for UFW 
ufw allow 4422/tcp 
systemctl status ufw 
Options: allow, deny, reject, limit 
ufw [rule] [target] 
ufw [rule] out [target] 
  
ufw app list 
ufw allow [App name] 
Run these commands 
 ufw allow ssh 
  
Eg. 
ufw allow in OpenSSH 
  
Limits 
Eg. ufw limit OpenSSH 
  
ufw [rule] from [ip_address] 
ufw deny from 192.168.100.20 
  
  
Use prepend to put rule to the top of the list 
ufw prepend deny from 192.168.100.20 
  
You can also target specific ports or port ranges with UFW 
ufw allow 8080 
  
Eg. 
ufw deny from 192.168.100.20 to any port 53 proto udp 
Target a network 
ufw allow in on eth0 from 192.168.100.255 
  
Log location: 
ls /var/log/ufw* 
  
Restart your configuration from scratch 
ufw reset
```