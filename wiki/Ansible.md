~~~
# Ansible 
add the ssh passkey to memory with ssh-add
ssh-add ~/SynologyDrive/ajay_data/ssh_keys/keyfile

-i points to inventory file
ansible-playbook -i inventory_ansible ping.yml

Inventory setup
all:
  vars:
    ansible_user: root
    ansible_ssh_private_key_file: ~/SynologyDrive/key_file
  hosts:
    ansible_container:
      ansible_host: 10.1.1.251
      
    synology_target:
      ansible_host: 10.1.1.5

    tailscale_exit_node:
      ansible_host: 10.1.1.102
    

    unifi_server:
      ansible_host: 10.1.1.2

    tenable_nessus:
      ansible_host: 172.22.22.103

    shonobi_server:
      ansible_host: 172.22.22.160

# My commonly run commands
ansible all –m ping
ansible-playbook updating_all_server_types.yml
FOR ALL HOSTS: 
ansible all –a "reboot now" 
For a SINGLE HOST: 
ansible uptime-kuma -a "reboot now"
ansible all –a "uptime"

Using a different inventory file
ansible-playbook install-samba.yml -i inventory.ini

## Ansible official docs: https://docs.ansible.com/ansible/2.7/user_guide/intro_getting_started.html
Yaml info and structure in another google doc: YAML syntax and structure


The ansible version in the Ubuntu repo is usually older than the PPA.

use ssh-agent to save the passphrase for the ssh-key so you are not prompted for the ssh passphrase on every server
ssh-agent bash then ssh-add path/agr-servers.key
ssh-add -l to list the key in use
Delete the SSH key from memory
ssh-add -D

Ubuntu install
$sudo apt install ansible
Check your installed version
$ansible --version



## Setting up ssh keys to access your servers
Generate a new key
$ssh-keygen -f ~/.ssh/labkeys_ssh -t ecdsa -b 521
Copy key to the server
$ssh-copy-id -i  ~/.ssh/labkeys_ssh ubu1@10.1.3.103
Test access with the key file
$ssh -i ~/.ssh/labkeys_ssh ubu1@10.1.3.103


Ubuntu servers
Getting no password prompt when using sudo
$sudo visudo
add this to the bottom of the file, change the username
username ALL=(ALL) NOPASSWD:ALL


## RUNNING A PLAYBOOK

ansible-playbook playbook name
Against a single host
ansible-playbook -i "PiHole01," updating_all_server_types.yml 
NOTE THE COMMA BEFORE THE LAST QUOTATION MARK

OR
ansible-playbook my_playbook.yml --limit my_host



## Managing Packages
So, we can manage the packages installed on all the hosts connected to ansible by using ‘yum’ & ‘apt’ modules & the complete commands used are


# Upgrade all the Ubuntu servers.
ansible hosts -m apt -a "upgrade=yes update_cache=yes" -b --become
Upgrade all the CentOS servers.
ansible hosts -m yum -a "name=* state=latest" -b


Check if package is installed & update it
$ ansible <group> -m yum -a “name=ntp state=latest”
Check if package is installed & don’t update it
$ ansible <group> -m yum -a “name=ntp state=present”
Check if package is at a specific version
$ ansible <group> -m yum -a “name= ntp-1.8 state=present”
Check if package is not installed
$ ansible <group> -m yum -a “name=ntp state=absent”



## Starting a service


$ ansible <group> -m service -a “name=httpd state=started”
Stopping a service


$ ansible <group> -m service -a “name=httpd state=stopped”
Restarting a service


$ ansible <group> -m service -a “name=httpd state=restarted”




Ansible notes from Acloud Guru 


Hosts file can be setup in folders other than /etc/ansible/hosts either:
1. pointing the adhoc command to the path of the inventory file by using the -i <path>
eg. #ansible -i /home/ansible_inventory --list-hosts all


2. The configuration file or environment variable can be set to point to the inventory file.
Changes can be made and used in a configuration file which will be searched for in the following order:


        ANSIBLE_CONFIG (environment variable if set)


        ansible.cfg (in the current directory)


        ~/.ansible.cfg (in the home directory)


        /etc/ansible/ansible.cfg


Ansible will process the above list and use the first file found, all others are ignored.


eg. of my ansible.cfg file, note the default username, the location of the SSH key file and the inventory key file are all specified.


ansible.cfg configuration file
[defaults]
inventory = ./inventory_ansible
remote_user = ec2-user
private_key_file = /home/ubu/Documents/anible_key_pairs.pem
host_key_checking = False


## Inventory file
[webservers]
web1 ansible_host=52.70.208.121
web2 ansible_host=34.197.18.113


[loadbalancers]
34.230.108.202


[local]
control ansible_connection=local
#Aliases in inventory file
web1 ansible_host=10.1.1.250
#Note: no spaces before and after equal sign.
______________________




## Playbooks


Running a playbook
$ansible-playbook playbookname -K
-K promt for sudo password




Using the example of an adhoc command: $ansible -m ping all
we convert this to a playbook. All ansible yaml files should start with --- at the top.
Then name or hosts must have a hyphen and spaced in for a total of 2 spaces [although it seems more than two spaces will work too, just not less than 2 spaces.]
Hosts: OR name: then tasks: is the usual listing. The first line after the 3 hyphens must have a - then hosts or name for a total space of 2.
Tasks fall directly under - hosts. After tasks space in and add a hyphen to each task in the list.
You can add a name for each task to enhance the stream as ansible runs the playbook.


ping playbook
---
  - hosts: all
    name: ping all servers
    tasks:
        -  name: ping time
           ping: ~


~ means all for ping?
or
---
   -name: this will ping
    hosts: all
    tasks:
• ping: ~



another example:


## This playbook is for updating servers
---
- name: updating apt packages
  hosts: all
  become: true
  tasks:
   - name: updates now
     apt: update_cache=yes force_apt_get=yes cache_valid_time=3600 upgrade=dist force_apt_get=yes


List of ansible ad-hoc commands
Running a shell command. ansible module shell -a is argument and the command in “quotes”, all is the group.
$ansible -m shell -a "df -h" all
or
$ansible -m shell -a "uptime" all


_____
You can use wildcards


$ansible --list-hosts “*”
or
$ansible --list-hosts app*


excluding control
$ansible --list-hosts \!control


 array syntax
$ansible --list-hosts webservers[0]


List two or more groups
$ansible --list-hosts webservers:loadbalancers


Variables


There are 3 ways to assign variables in ansible.


1. Many variables can be made from the facts gathered when a playbook is executed.
running the setup module on server app1 shows you the system details and the variables denoted by ansible_   [Not completely sure all “gathering facts” variables start with ansible_]


$ansible -m setup app1


2. You can use vars to import your own variables from another file or within the same playbook file.
Below is an example of two variables in a dictionary:
NOTE: ‘{{ ONE SPACE ON EACH END WITHIN THE PARENTHESIS }}”
NOTE: the double quote are optional - and will cause an error if using it in a file path
---
  vars: 
    file_path: “/vars/www/html”
    other_variable: “monkey”
  tasks:
• name: copy file
copy:
  destination: “{{ file_path }}/info.php”
  content: “<h1>Hello, World</h1>”


3. Register variables from tasks that get run with the register entry in a playbook:
You can use debug to view the contents of variables or debug a playbook.


---
  vars:
  path_to_app: “/var/www/html”


  hosts: all
  tasks:
• name: see directory contents
command: ls -la {{ path_to_app }}
register: dir_contents


• name: debug dir contents
debug:
   msg: “{{ dir_contents }}”



Adding ansible variable data to the index.html on a webserver


insertbefore – This should be set to BOF to make sure the line is added at the beginning. If the pattern already exists it won’t be added. So executing again won’t add more lines.
take a variable and display it, then publish to the webserver
---
 - name: playing with variables
   become: true
   hosts: app
   tasks:
    - name: display the webserver ip addresses from facts gathered  [ansible -m setup app]
      debug:
        msg: "{{ ansible_all_ipv4_addresses }}"
 
    - name: take the ip4 addresses and list them in the web server
      lineinfile:
        path: /var/www/html/index.html
        regexp: '^<h1>'
        line: '<h1>"{{ ansible_all_ipv4_addresses }}"</h1>'
 
    - name: add hostname
      lineinfile:
        path: /var/www/html/index.html
        line: '<h1>"{{ ansible_hostname }}"</h1>'
        insertbefore: BOF



Example of variable with lineinfile:
 - hosts: srv0
   become: true
   tasks:
     - name: Download the deb file
       get_url:
         url: https://repo.zabbix.com/zabbix/5.2/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.2-1+ubuntu20.04_all.deb
         dest: /home/{{ ansible_user }}


~~~
