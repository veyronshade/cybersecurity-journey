# Wireshark: Traffic Analysis - TryHackMe Writeup
> **Platform:** TryHackMe  
> **Room:** Wireshark: Traffic Analysis     
> **Difficulty:** Medium  
> **Date Completed:** May 2026  
> **Category:** Network Security / SOC / Forensics

---

## What This Room Is About

This room explains how to look at real network traffic to understand what is happening inside a network, such as scanning for devices, stealing or redirecting traffic, identifying users and machines, and spotting hidden or suspicious communication. It shows how attackers use common network tools and protocols like Nmap, ARP, DNS, HTTP, FTP, and HTTPS in both normal and malicious ways, and how analysts can recognize unusual patterns like spoofing, tunneling, or exposed passwords. This matters in the real world because it helps security analysts detect attacks early, understand how systems are being targeted, and take action to stop hackers before they cause damage.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Wireshark | Used to capture and analyze network traffic to detect Nmap-based scanning activity (TCP Connect, SYN, and UDP scans) by filtering TCP flags, ports, and ICMP responses |
| Wireshark | Used to isolate scan patterns such as tcp.flags.syn==1, tcp.flags.ack==0, and icmp.type==3 to identify reconnaissance activities like SYN scans and UDP scans |
| Wireshark | Used to understand protocol distribution in captured traffic and quickly spot abnormal spikes in TCP/UDP traffic associated with port scanning behavior |
| Wireshark	| Used to identify scanning sources by analyzing communication patterns between IPs, ports, and endpoints involved in reconnaissance activity |
| Wireshark | Used to inspect raw packet behavior (SYN-only attempts, reset responses, ICMP unreachable messages) to distinguish TCP Connect scans, SYN scans, and UDP scan responses |

---

## Key Concepts Covered

- **Nmap Scans (TCP Connect, SYN, UDP scans)** — I learnt how to recognize different types of network scanning in Wireshark by observing TCP flags, handshake behavior, and ICMP responses to detect reconnaissance activity on a target system.
- **ARP Poisoning & Man-in-the-Middle (MITM)** — I learnt how to detect when an attacker is spoofing ARP messages to trick devices into sending traffic through them so they can secretly intercept or modify network communication.
- **Identifying Hosts (DHCP, NetBIOS, Kerberos)** - I leant how to identify users, devices, and domain activity in a network by analyzing DHCP leases, NetBIOS name queries, and Kerberos authentication tickets to understand who is who in the traffic.
- **Tunneling Traffic (ICMP and DNS)** - I leant how attackers hide data or command-and-control communication inside normal ICMP or DNS traffic by spotting unusual packet sizes, long queries, or abnormal request patterns.
- **Cleartext Protocol Analysis (FTP)** — I learnt how to inspect unencrypted FTP traffic to detect exposed usernames, passwords, and file transfers that can be easily captured during an attack or misconfiguration.
- **Cleartext Protocol Analysis (HTTP)** - I learnt how to analyze unencrypted web traffic to identify malicious requests, suspicious URLs, status codes, and attack behavior like phishing or web exploitation.
- **User Agent Analysis (HTTP)** -  I learnt how to detect suspicious tools or attackers by examining the User-Agent field for anomalies, scanning tools like Nmap, or inconsistent browser identity strings.
- **Log4j Analysis (HTTP exploitation patterns)** - I learnt how to identify Log4j exploitation attempts in HTTP traffic by spotting malicious payload patterns like JNDI lookups and unusual POST requests used for remote code execution.
- **Encrypted Protocol Analysis (HTTPS Decryption)** - I learnt how to investigate encrypted HTTPS traffic by using TLS handshake visibility and key log files to decrypt sessions and inspect hidden web communication.
- **Hunt Cleartext Credentials** - I learnt how Wireshark automatically or manually extracts exposed usernames and passwords from insecure protocols like FTP, HTTP, SMTP, and IMAP for brute-force or compromise detection.
- **Actionable Results (Firewall Rules from Wireshark)** - I learnt how to convert identified malicious IPs, ports, or MAC addresses from packet analysis into real firewall rules to immediately block or contain an attack in a live environment.

---

## Commands Used and What They Do

This investigation was carried out using Wireshark packet capture analysis.
Instead of traditional CLI tools, display filters were used to isolate malicious traffic patterns, identify attacks, and extract forensic evidence.

- **🔎 Reconnaissance**
```bash
    tcp.flags.syn == 1 and tcp.flags.ack == 0

#What it does:
#Detects initial SYN packets
#Used to identify Nmap SYN scans (stealth reconnaissance)
#Helps spot port scanning activity before exploitation
```
---
- **🧨 MITM Attack**
```bash
    arp.duplicate-address-detected

#What it does:
#Detects multiple MAC addresses claiming the same IP
#Strong indicator of ARP spoofing / Man-in-the-Middle (MITM) attack
#Used to identify network-level interception attempts
```
---
- **🌐 Data Exfiltration / C2**
```bash
    dns.qry.name.len > 15 and !mdns

#What it does:
#Detects abnormally long DNS queries
#Used to identify DNS tunneling / C2 communication
#Common in malware data exfiltration over DNS
```
---
- **🕵️ Attacker Tool Detection**
```bash
    http.user_agent contains "nmap"

#What it does:
#Detects network scanning tools hidden in HTTP headers
#Helps identify reconnaissance activity (Nmap, sqlmap, Nikto)
#Shows attacker fingerprinting behavior in web traffic
```

---

## What I Found / What Happened (Walkthrough Summary)

I performed a structured traffic analysis using Wireshark to investigate multiple simulated network attack scenarios from a SOC analyst perspective. He identified Nmap scanning patterns by analyzing TCP flags, distinguishing between TCP Connect, SYN, and UDP scans based on handshake behavior and response anomalies. I was able to detect ARP poisoning activity by observing duplicate IP-to-MAC mappings and confirmed a Man-in-the-Middle situation through redirected traffic flows. I further analyzed host identification and authentication traffic using DHCP, NetBIOS, and Kerberos to map users, devices, and domain activity, while also investigating tunneling attempts in ICMP and DNS through abnormal payload sizes and query patterns. Finally, I examined cleartext and encrypted application traffic (FTP, HTTP, and HTTPS), uncovered potential credential exposure, analyzed malicious indicators like Log4j exploitation attempts, and demonstrated how findings can be escalated into actionable firewall rules for containment and response.

---

## Key Takeaways

- Takeaway 1: I learnt that every cyberattack leaves a network pattern behind, and Wireshark makes those patterns visible. From Nmap TCP/SYN/UDP scans to ARP poisoning, DNS tunnelling, ICMP abuse, FTP credential theft, suspicious HTTP traffic, and Log4j exploitation attempts, I learnt how attackers communicate on the network and how a traffic analyst can detect those behaviours through packet analysis and filtering.

- Takeaway 2: I learnt that protocols reveal identity, behaviour, and intent. By analysing DHCP, NetBIOS (NBNS), and Kerberos traffic, I learned how SOC analysts identify hosts, users, devices, domains, authentication activity, and suspicious communications inside a network. I also learned that understanding protocols deeply is the foundation of both ethical hacking and defensive security analysis.

- Takeaway 3: I learnt that packet analysis is not just about observing traffic but it is about turning findings into actionable security decisions. Through HTTPS decryption, cleartext credential hunting, user-agent analysis, and firewall ACL generation, I learned how analysts investigate encrypted and unencrypted traffic, detect attacks and stolen credentials, trace attacker activity, and create defensive responses to protect the network.

---

## How This Applies to Real-World Security

A SOC analyst would use these Wireshark traffic analysis skills to investigate suspicious activities like Nmap scans, ARP spoofing, DNS tunnelling, malicious HTTP traffic, credential theft, and encrypted HTTPS communications detected from SIEM alerts or network monitoring tools. Understanding how to identify hosts through DHCP, NetBIOS, and Kerberos traffic while detecting anomalies in ICMP, DNS, FTP, and HTTP communications helps analysts quickly separate normal behaviour from malicious activity. From a penetration tester’s perspective, understanding how these attacks appear in packet captures helps simulate realistic attacks, understand what defenders can see, and improve both offensive and defensive security skills.

---

## References

- [TryHackMe Room Link](https://tryhackme.com/room/wiresharktrafficanalysis)
- Wireshark


---

*Written by Precious Ajibola | TryHackMe Profile: [VeyronShade](https://tryhackme.com/p/VeyronShade) | LinkedIn Profile: [Precious Ajibola](https://www.linkedin.com/in/precious-ajibola-b086ab173)*
