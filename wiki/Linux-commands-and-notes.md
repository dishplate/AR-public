# Linux commands and Notes
## Zip and Unzip 

If you need to decompress multiple files  you have to place the *.zip in quotes. 
unzip '*.zip' 

## Find Command

https://www.tecmint.com/35-practical-examples-of-linux-find-command/ 
 
 
find /etc -name ssh -type f 
Above searches /etc for a  file named ssh 
-type f     file 
-type d     directory 
-perm   for permissions eg. -perm 770 
-exec    for executing a command against search results 
-iname  for ignoring case eg. *.jpg will also find *.JPG 
-user    find a user 
~~~
Find all the files whose name is tecmint.txt in a current working directory. 
# find . -name tecmint.txt 
 
To find all or single files called tecmint.txt under / root directory of owner root. 
# find / -user root -name tecmint.txt 
 
Find all directories whose name is Tecmint in / directory. 
# find / -type d -name Tecmint 
 
Find all the files whose permissions are 777. 
Find by size 
find . -size +2G 
find . -size –2G 
~~~
Grep
grep –v   
will invert your search 
 
++++++ 
## Grep through all files and folders 
 
grep -rni "string" * 
 
 
where 
* r = recursive i.e, search subdirectories within the current directory 
* n = to print the line numbers to stdout 
* i = case insensitive search 

## Mounting file systems
~~~
Mount CIFS share
Make sure the user mounting has permissions to the folders and files on the NAS.
Make sure the user on Synology has access to the SMB/share app.
Double check the username and password
Make a credential file on the client system and chmod 600 the file.
The file should contain
username=test
password=test123

mkdir a folder and you might need to make sure that the user mounting the share has
Access to the same folder, chown user mount_folder

Command to run
mount -t cifs -o credentials=/root/credfile //10.5.5.250/tar_files /nas_mount
You might get some weird errors but check if it worked anyway
dmesg to troubleshoot
~~~


