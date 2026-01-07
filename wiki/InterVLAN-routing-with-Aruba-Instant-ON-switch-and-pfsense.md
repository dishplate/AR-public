~~~
Got it to work.
1. Turn on routing in the aruba and setup a gateway of 10.1.1.1
2. You don't need a GW per each VLAN as I thought
3. No need to tweak anything in pfsense except FW rules. Some traffic will have issues such as asymmetric routing if both devices don't have the same GW or GW that points to Aruba. 
4. You might have rules come in through the LAN for another network and some other rules will be managed as expected on their own vlan - not sure why.
5. You can add an easy rule for testing and see where it goes.
6. DHCP relay is ON for port 24

~~~