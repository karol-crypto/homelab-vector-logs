# homelab-vector-logs
A low-spec log pipeline solution: collecting OPNsense logs via UDP, processing them through an Ubuntu-hosted Vector relay, and securely forwarding JSON-formatted events to a Windows-based Python HTTP receiver for SecOps and homelab analysis.

To build this project I used the GNS3 environment for the network setup and VirtualBox. To avoid overloading one computer I used a Cloud object in GNS3 to connect a second physical computer. 

At this stage of the lab devices don't have internet access.


Detailed description of the topology you can find --> [here](topology) 
