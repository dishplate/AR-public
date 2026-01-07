# Quick Netcat commands

### Check if a port is open
nc -z host.example.com 20-30
Example of output:
Connection to 172.16.134.131 port 3389 [tcp/ms-wbt-server] succeeded!

### File transfer with nc
Start by using nc to listen on a specific port, with output captured
     into a file:

           $ nc -l 1234 > filename.out

     Using a second machine, connect to the listening nc process, feeding it
     the file which is to be transferred:

           $ nc host.example.com 1234 < filename.in

     After the file has been transferred, the connection will close
     automatically.

