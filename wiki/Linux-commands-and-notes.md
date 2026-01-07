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
 
