Internet is a world wide connection of interconnected networks
LAN’S: can local networks , small, medium  to world wide
Bits
A network is when end to end devices connect to each other so they can exchange data

Terms: 
End devices (hosts): where data starts or finishes. PCs, phones, servers, printers, IP cameras.
Intermediary devices: move data between hosts. Switches, routers, wireless access points, firewalls.
Media: the path the signal travels. Copper cable, fibre-optic cable, or radio waves.
Client-Server: good for scaling, better security
Peer to Peer: low cost, easy to setup


LAN: One building or campus, one administrator, high speed	
WLAN: A LAN using radio instead of cable	
WAN: Connects LANs over large distances, usually through a service provider	
Internet: The global collection of interconnected networks	
Intranet / Extranet: Private network for one organisation / extended to selected outsiders	
Hub (obsolete): Nothing Repeats every bit out of every port; one shared collision domain
Switch: MAC addresses; Forwards frames only to the port where the destination lives, inside one LAN
Router: IP addresses; Forwards packets between different networks; the boundary of a broadcast domain
Wireless access point: MAC addresses; Bridges Wi-Fi clients onto the wired LAN
Firewall: Rules and connection state; Permits or blocks traffic by policy
Network characteristics
Fault tolerance: redundant paths so one failure does not cut service.
Scalability: grows without redesign.
Quality of Service (QoS): voice and video get priority over bulk downloads.
Security: confidentiality, integrity, availability (the CIA triad).
Rules of communication
Encoding: How is information turned into a transmittable form? Bits become voltages, light pulses, or radio waves. 
Formatting and Encapsulation: What structure does a message have? A frame with addresses in a header and a checksum in a trailer. 
Message Size: How large may one message be? Long data is split into frames of at most 1500 bytes of payload. 
Timing: Flow Control: How fast may the sender send? TCP window size. 
Timing: Response Timeout: How long to wait for a reply? TCP retransmission timer. 
Timing: Access Method: When may a device use the shared medium? CSMA/CA on Wi-Fi. 
Delivery Options: One, some, or all recipients? Unicast, multicast, broadcast. 
OSI MODEL
7. Application: HTTP, DNS, DHCP, SMTP, SSH (Data)
6. Presentation: Encoding, encryption, compression - TLS, JPEG (Data)
5. Session: Opens, manages and closes dialogues (Data)
4. Transport: TCP, UDP, port numbers (Segment / Datagram)
3. Network: IPv4, IPv6, ICMP, routers (Packet)
2. Data Link: Ethernet, 802.11, MAC, switches (Frame)
1. Physical: Cables, connectors, signals, radio (Bits)


TCP/IP Model
Application: OSI equivalent 7, 6, 5. Protocols: HTTP, HTTPS, DNS, DHCP, FTP, SMTP, SSH.
Transport: OSI equivalent 4. Protocols: TCP, UDP.
Internet: OSI equivalent 3. Protocols: IPv4, IPv6, ICMP.
Network Access: OSI equivalent 2, 1. Protocols: Ethernet, Wi-Fi, ARP.
Encapsulation: As data moves down the stack, layers add headers (and Ethernet adds an FCS trailer); de-encapsulation strips them in reverse.
L7 Data: GET /index.html HTTP/1.1 …
L4 Segment: TCP hdr (src 51544, dst 80) + Data
L3 Packet: IP hdr (192.168.10.11 → 198.51.100.10) + TCP hdr + Data
L2 Frame: Eth hdr (dst MAC of gateway) + IP + TCP + Data + FCS
L1 Bits: 0110100101110011…
Segmentation, Multiplexing, and Sequencing: Large files are segmented so multiple conversations can interleave on one link (multiplexing). Sequencing ensures correct reassembly and selective resends without blocking the network.
Network Metrics
Bandwidth: The capacity of a medium—bits per second it can carry (bps, kbps, Mbps, Gbps, Tbps).
Throughput: Bits actually transferred per second; usually below bandwidth because of traffic, errors, and device limits.
Goodput: Usable data per second—throughput minus protocol overhead, retransmissions, and handshakes.
Latency: Delay for data to travel from one point to another, including queuing.
