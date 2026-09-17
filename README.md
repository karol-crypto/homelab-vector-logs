# homelab-vector-logs
A low-spec log pipeline solution: collecting [OPNsense](OPNsense) logs via UDP, processing them through an [Ubuntu](UbuntuServer)-hosted Vector relay, and securely forwarding JSON-formatted events to a Windows-based Python HTTP receiver for SecOps and homelab analysis.

To build this project I used the GNS3 environment for the network setup and VirtualBox. To avoid overloading one computer I used a Cloud object in GNS3 to connect a second physical computer. 

The logs are received by python script 

    log_script_receiver.py

For the script to work we should allow http port in Windows Firewall. To do this we can use this command in PowerShell: 
    
    New-NetFirewallRule -DisplayName "Python HTTP Log Receiver" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow


At this stage of the lab devices don't have internet access.


Detailed description of the topology you can find [here](Topology) 
