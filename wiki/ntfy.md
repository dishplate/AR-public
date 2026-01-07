# ntfy setup
https://docs.ntfy.sh/install/#debianubuntu-repository
## Send a message with command results 
scan=$(nmap 10.1.1.250) && curl -d "results of nmap $scan)" 172.22.22.12/test

### Notes
Seems to only work with http