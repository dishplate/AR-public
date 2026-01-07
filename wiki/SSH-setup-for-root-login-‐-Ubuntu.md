# SSH
By default root login is not permitted
Edit this file: 
nano /etc/ssh/sshd_config
Uncomment this line and add yes:

PermitRootLogin     yes

Another option if you want keys used instead of passwords:

PermitRootLogin prohibit-password

# Restart the service
systemctl restart ssh.service
or some systems have it name differently

# Troubleshooting
systemctl status ssh.service" and "journalctl -xeu ssh.service" for details

