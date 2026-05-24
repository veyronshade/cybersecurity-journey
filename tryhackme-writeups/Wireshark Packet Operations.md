# Wireshark: Packet Operations — TryHackMe Writeup

> **Platform:** TryHackMe  
> **Room:** Wireshark: Packet Operations  
> **Difficulty:** Easy  
> **Date Completed:** May 2025  
> **Category:** Network Security

---

## What This Room Is About

Wireshark covers how computers and devices communicate with each other across a network, how information travels between systems, and how to isolate specific activities from huge amounts of traffic so you can clearly see what is happening. It also teaches how to track website activity, identify where connections are coming from or going to, organize investigations using filters, profiles, and bookmarks, and quickly spot unusual or suspicious behavior inside network communication. In the real world, this matters because SOC Analysts and Ethical Hackers use these skills to investigate cyberattacks, detect malware, trace suspicious connections, understand how applications communicate, and uncover security problems hidden inside normal-looking network traffic.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Statistics (Protocol Details) | Helps analysts understand overall network activity such as IPv4/IPv6 traffic, DNS requests, and HTTP communication. |
| Packet Filtering | Reduces network noise and allows analysts to focus only on suspicious or important packets during investigations. |
| Capture Filters | Captures only specific traffic before recording packets, helping reduce unnecessary data collection. |
| Display Filters | Displays only selected packets after capture, making traffic analysis faster and easier for SOC Analysts and Ethical Hackers. |
| Protocol Filters (IP, TCP, UDP, HTTP, DNS) | Filters packets based on IP addresses, ports, protocols, web traffic, and DNS activity to investigate attacks and communication patterns. |
| Advanced Filtering, Bookmarks & Profiles | Helps analysts perform deeper investigations using advanced searches, save favorite filters, and create custom analysis workspaces for different security tasks. |

---

## Key Concepts Covered
- **Statistics (Protocol Details)** — I learnt that Wireshark statistics help analysts understand the overall network activity by showing important protocol information such as IPv4, IPv6, DNS, and HTTP traffic patterns.
- **Packet Filtering Principles** — I learnt that packet filtering helps reduce massive network traffic into relevant packets using capture filters and display filters for easier investigation and analysis.
- **Application Level Protocol Filters and Display Filter Expressions** — I learned that HTTP and DNS filters allow analysts to inspect application-level activities such as website requests and DNS lookups, while display filter expressions help create accurate filters more easily.
- **Advanced Filtering, Bookmarks, Filtering Buttons, and Profiles** — I learned that advanced filtering features like contains, matches, and in help analysts perform deeper traffic analysis, while bookmarks, filter buttons, and profiles improve speed and organization during investigations.

---

## Commands Used and What They Do

- **Statistics (Protocol Details)** - These commands were used to understand the overall network behavior and traffic composition.

```bash
# IPv4 / IPv6 Analysis
- Shows whether the network is using IPv4, IPv6, or both.
- Helps identify addressing structure and protocol usage trends.
```

```bash 
# DNS Statistics
- Displays DNS queries and responses.
- Helps identify domain lookups, request patterns and potential malicious domains.
```

```bash
# HTTP Statistics
- Shows HTTP request/response distribution.
- Helps analyze web activity, response codes (200, 404, etc.) and  request types (GET, POST).
```

- **Packet Filtering (Principles)** - Wireshark filtering was used to isolate relevant traffic from large packet captures.

```bash
# In this investigation, display filters were mainly used.
Examples are; 
- tcp port 80   #(Captures HTTP traffic at the transport layer.)
- ip.addr == 10.10.10.111   #(Shows all packets involving a specific IP address.)
```

- **Protocol-Based Filtering** 
```bash
# IP Layer Filters
- ip.addr == 10.10.10.0/24 
#(Filters all traffic within a subnet.)
- ip.src == 10.10.10.111
- ip.dst == 10.10.10.111
#(Filters traffic by source or destination IP.)

# TCP / UDP Filters
- tcp.port == 80
- udp.port == 53

# Filters traffic by service ports:
- HTTP (80)
- DNS (53)
```

- **Application Layer Filters** 
```bash
# HTTP Filters
- http
#(Shows all HTTP traffic.)

- http.request.method == "GET"
- http.request.method == "POST"
#Identifies web requests:
# GET - data retrieval
# POST - data submission

- http.response.code == 200
#(Shows successful HTTP responses)

# DNS Filters
- dns
#(Displays all DNS traffic)

- dns.flags.response == 0
#(Shows DNS queries only.)

- dns.qry.type == 1
#(Filters A-record lookups (domain to  IP resolution))
```

- **Advanced Filtering Techniques** - These filters were used for deeper investigation and pattern detection.

```bash
- http.server contains "Apache"
#(Searches for specific server types in HTTP traffic)

- http.host matches "\.(php|html)"
#(Uses regex to filter specific file types)

- tcp.port in {80 443 8080}
#(Filters multiple ports in a single query.)

- string(frame.number) matches "[13579]$"
#(Converts frame numbers to string and filters odd-numbered packets)
```

- **Bookmarks & Filter Buttons** - Frequently used filters were saved for quick reuse and improved speed and efficiency during analysis.

- **Profiles** - Custom Wireshark profiles were used to switch between investigation setups and it helps separate workflows such as; *web traffic analysis, DNS investigation and general packet inspection*.

---

## Walkthrough Summary

In this room, I used Wireshark to analyze network traffic by focusing on protocol statistics, packet filtering, and advanced filtering techniques. I reviewed IPv4 and IPv6 statistics to understand the types of IP traffic present in the capture, and I also analyzed DNS and HTTP statistics to identify domain requests, web activity, and protocol usage patterns. I practiced using both capture filters and display filters, including comparison and logical operators, to isolate specific packets based on IP addresses, ports, HTTP requests, and DNS queries. I further explored protocol specific filters such as IP, TCP, UDP, HTTP, and DNS filters to investigate communication behavior across different OSI layers. In addition, I used advanced filtering techniques like contains, matches, and in operators, while also learning how bookmarks, filter buttons, and profiles can improve investigation efficiency and workflow organization during packet analysis.


---

## Key Takeaways

1. Wireshark statistics like IPv4/IPv6, DNS, and HTTP help me quickly understand who is communicating, what websites are being accessed, and what type of traffic exists on the network.

2. Display filters are one of the most powerful Wireshark features because they allow me to search and isolate specific traffic using IPs, ports, protocols, operators, and logical expressions during investigations.

3. Advanced filtering, bookmarks, filter buttons, and profiles help SOC Analysts and Ethical Hackers investigate traffic faster, organize investigations better, and detect suspicious or malicious network activity more efficiently.
---

## How This Applies to Real-World Security

A SOC analyst would use protocol statistics such as IPv4/IPv6, DNS, and HTTP details to quickly identify suspicious communication, unusual DNS requests, or abnormal web traffic during an incident investigation. Packet filtering and advanced display filters allow analysts and penetration testers to isolate specific IP addresses, ports, protocols, and malicious patterns from millions of packets, making threat hunting and traffic analysis far more efficient. Features such as filter expressions, bookmarks, filtering buttons, and profiles help security professionals automate repetitive investigations, speed up incident response, and maintain organized workflows when analyzing real-world network attacks.


---

## References

- [TryHackMe Room Link](https://tryhackme.com/room/wiresharkpacketoperations)
- Wireshark


---

*Written by Precious Ajibola | TryHackMe Profile: [VeyronShade](https://tryhackme.com/p/VeyronShade) | LinkedIn Profile: [Precious Ajibola](https://www.linkedin.com/in/precious-ajibola-b086ab173)*
