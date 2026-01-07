~~~
Setup linux vm or container
enable ufw - see my other instructions on ufw in github

Setup your exit node after installing the tailscale software
https://tailscale.com/kb/1103/exit-nodes?tab=ios

Use your exit node as a router
https://tailscale.com/kb/1019/subnets
Remember to use the advertising of the route like this:
tailscale up --advertise-routes=10.1.1.0/24 --advertise-exit-node

Check your connections
sudo lsof -nP -i


~~~