# Wireshark (The Basics) — TryHackMe Writeup

> **Platform:** TryHackMe  
> **Room:** Wireshark (The Basics)  
> **Difficulty:** Easy  
> **Date Completed:** May 2025   
> **Category:** Networking

---

## What This Room Is About

This room teaches how to watch and understand the communications happening between computers on a networks using a tool called Wireshark. It shows how to spot noraml activity, suspicious behaviour and hidden problems by looking attentively at the information devices send to each other online. In the real world, this matters because ethical hackers, SoC analysts and IT professionals use these skills to investigate cyberattacks, troubleshoot network issuses and protect organisations from threats.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Wireshark | Capturing and analyzing network packets |
| Wireshark Toolbar | Accesing the tools for capturing, analyzing, filtering and seatching packets |
| Packet List Pane  | Viewing a summary of all captured packets
| Packet Byte Pane | Viewing detailed breakdown of the selected packet through the OSI layers|
| Packet Details Pane | Viewing the raw packet data in hexadecimal and readable text|

---

## Key Concepts Covered

- **Packet Analysis** — I learnt that Wireshark captures and breaks down network packets so I can see how devices communicate across a network in real time.
- **OSI Layers in Action** — I understood that every packet passes through different network layers like MAC addresses, IP addresses, ports, and application protocols, and Wireshark helps me see each layer clearly.
- **Traffic Filtering** — I learnt that display filters help me remove unnecessary traffic and focus only on suspicious protocols, IP addresses, ports, or conversations during analysis.

---

## What I Found / What Happened (Walkthrough Summary)

1. I loaded the “Exercise.pcapng” file in Wireshark and examined the capture file metadata and comments to understand the context of the traffic and identify the hidden flag embedded in the file details.
2. This revealed key capture statistics such as the total packet count (58,620) and the SHA256 hash of the file, helping confirm the integrity and scale of the dataset being analyzed.
3. I moved into packet dissection, inspecting specific packets (like packet 38) to analyze HTTP-layer details such as XML content, TTL values, TCP payload size, timestamps, and E-tag information.
4. Using packet navigation and search functions, he located specific strings like “r4w” and examined packet comments and embedded files, uncovering hidden artifacts including an MD5 hash and a file containing the alien name “PACKETMASTER.”
5. I applied display filters and HTTP stream analysis to isolate web traffic, reducing noise from 58,620 packets to relevant flows, which allowed him to extract structured data such as artist names and confirm there were 3 artists in total, including “Blad3” as the second artist.

---

## Key Takeaways

- Wireshark is a network “CCTV” that lets me see raw network communication in real time. It helps me observe and analyze traffic
- Every packet I see represents data moving through the OSI layers (MAC → IP → TCP/UDP → Application), and understanding these layers is key to truly understanding how both networking and the internet actually work
- Filters, stream following, and packet inspection are the main power tools in Wireshark—they let me cut through noise, trace communications, and detect suspicious network behaviour

---

## How This Applies to Real-World Security

In a real SOC environment, an analyst uses Wireshark packet analysis to investigate alerts from SIEM tools by digging down into raw network traffic and confirming whether activity is normal or malicious. Being able to interpret packet layers, follow streams, and apply filters helps quickly identify issues like credential leakage, suspicious connections, or malware communication patterns. For a penetration tester, the same skills are used to verify vulnerabilities by observing how data flows across the network and confirming whether sensitive information is exposed in transit.

---

## References

- [TryHackMe Room Link](https://tryhackme.com/room/wiresharkthebasics) 
- Wireshark


---

*Written by [Precious Ajibola] | TryHackMe Profile: [VeyronShade](https://tryhackme.com/p/VeyronShade) | LinkedIn Profile: [Precious Ajibola](https://www.linkedin.com/in/precious-ajibola-b086ab173)*
