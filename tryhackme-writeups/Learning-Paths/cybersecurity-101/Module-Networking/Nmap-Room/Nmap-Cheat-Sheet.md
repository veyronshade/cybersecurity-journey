# 🗂️ Nmap Cheat Sheet

## Host Discovery
| Command | Description |
|---------|-------------|
| `nmap -sn 192.168.1.0/24` | Ping sweep (no port scan) |
| `nmap -Pn target` | Skip host discovery, scan all |
| `nmap -PS target` | TCP SYN ping |
| `nmap -PA target` | TCP ACK ping |
| `nmap -PU target` | UDP ping |

## Port Scanning
| Command | Description |
|---------|-------------|
| `nmap -p 80 target` | Scan single port |
| `nmap -p 1-100 target` | Scan port range |
| `nmap -p- target` | Scan all 65535 ports |
| `nmap --top-ports 100 target` | Scan top 100 ports |
| `nmap -F target` | Fast scan (top 100) |

## Scan Types
| Command | Description |
|---------|-------------|
| `sudo nmap -sS target` | TCP SYN (stealth) |
| `nmap -sT target` | TCP Connect |
| `sudo nmap -sU target` | UDP scan |
| `sudo nmap -sA target` | ACK scan |
| `sudo nmap -sW target` | Window scan |
| `sudo nmap -sM target` | Maimon scan |
| `sudo nmap -sN target` | TCP Null scan |
| `sudo nmap -sF target` | TCP FIN scan |
| `sudo nmap -sX target` | TCP Xmas scan |

## Service & OS Detection
| Command | Description |
|---------|-------------|
| `nmap -sV target` | Service version detection |
| `sudo nmap -O target` | OS detection |
| `sudo nmap -A target` | Aggressive (OS + version + scripts + traceroute) |
| `nmap --version-intensity 5 target` | Version detection intensity (0-9) |



## Output Formats
| Command | Description |
|---------|-------------|
| `nmap -oN file.txt target` | Normal (human-readable) |
| `nmap -oX file.xml target` | XML format |
| `nmap -oG file.gnmap target` | Grepable format |
| `nmap -oA basename target` | All three formats |
| `nmap -v target` | Verbose output |
| `nmap -vv target` | Very verbose |

## Performance & Timing
| Command | Description |
|---------|-------------|
| `nmap -T0 target` | Paranoid (IDS evasion) |
| `nmap -T1 target` | Sneaky |
| `nmap -T2 target` | Polite |
| `nmap -T3 target` | Normal (default) |
| `nmap -T4 target` | Aggressive |
| `nmap -T5 target` | Insane |
| `nmap --max-retries 1 target` | Limit retries |
| `nmap --host-timeout 30s target` | Host timeout |
| `nmap --max-rtt-timeout 100ms target` | RTT timeout |


## Useful Combinations
```bash
# Comprehensive scan
sudo nmap -sS -sV -O -p- -A -oA full-scan target

# Quick but thorough
sudo nmap -sS -sV -T4 -oA quick-scan target

# UDP focus
sudo nmap -sU --top-ports 100 -T4 target

# Stealth + scripts
sudo nmap -sS -sC -T2 -oN stealth-scan.txt target
```
