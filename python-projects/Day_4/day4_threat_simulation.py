import random

# PART 1: DATA STRUCTURES
attack_types = ["Phishing", "Ransomware", "DDoS Attack", "SQL Injection", "Brute Force", "Man-in-the-Middle"]
soc_team = ['Veyron', 'Detective', 'Inspector', 'Root', 'Inquisitor']
severity_levels = ['Minimal', 'low', 'Moderate', 'Severe', 'Critical']
target_systems = [["Web Server Alpha", "192.168.1.10", "HIGH"],
                  ["Web Server Bravo", "192.168.1.28", "LOW"],
                  ["Web Server Tango", "192.168.1.56", "MEDIUM"],
                  ["Web Server SIGMA", "192.168.1.92", "HIGH"],
                  ["Web Server Beta", "192.168.1.35", "LOW"]]

print("=====================================================")
print(f"First attack type               : {attack_types[0]}")
print(f"Last attack type                : {attack_types[-1]}")
print(f"Third Analyst                   : {soc_team[2]}")
print(f"System 2 name                   : {target_systems[1][0]}")
print(f"System 4 IP                     : {target_systems[3][1]}")
print(f"System 1 sensitivity            : {target_systems[0][2]}")
print("=====================================================\n \n")

# PART 2: INDEX VERIFICATION
print("===== INDEX VERIFICATION =====")
print(f"First attack type       :{attack_types[0]}")
print(f"Last attack type        : {attack_types[-1]}")
print(f"Third analyst           : {soc_team[2]}")
print(f"System 2 name           : {target_systems[1][0]}")
print(f"System 4 IP             : {target_systems[3][1]}")
print(f"System 1 sensitivity     : {target_systems[0][2]}")
print("==============================")


# PART 3: RANDOM SIMULATION ENGINE
random_attack = random.choice(attack_types)
random_soc = random.choice(soc_team)
random_target = random.choice(target_systems)
random_severity = random.choice(severity_levels)

threat_score = random.randint(1, 100)
affected_users = random.randint(1, 500)
hours = random.randint(2, 72)

selected_target = random_target[0]
selected_ip_addr = random_target[1]
selected_sensitivity_level = random_target[2]

#  PART 4: INCIDENT LOG
incident_log = []
incident_log.append("INCIDENT INITIATED")
incident_log.append(random.choice(attack_types))
incident_log.append(random.choice(soc_team))
incident_log.append(selected_target)
incident_log.append("STATUS: UNDER INVESTIGATION")
entry_length = len(incident_log)

print("\n \n--- INCIDENT LOG VERIFICATION ---")
print(incident_log[0])
print(incident_log[2])
print(incident_log[-1])
print(f"Total entries:  {entry_length}")
print("----------------------------------\n \n")

# PART 5: FULL INCIDENT
print("============================================")
print("CYBERSHIELD THREAT SIMULATION ENGINE\nINCIDENT REPORT — AUTO-GENERATED")
print("============================================")
print(f"Attack Vector           : {random_attack}")
print(f"Lead Analyst            : {random_soc}")
print("--------------------------------------------")
print(f"Target System           : {selected_target}")
print(f"System IP               : {selected_ip_addr}")
print(f"Data Sensitivity        : {selected_sensitivity_level}")
print("--------------------------------------------")
print(f"Threat Score            : {threat_score}/100")
print(f"Users Affected          : {affected_users}")
print(f"Recovery Time           : {hours} hours")
print(f"Severity Level          : {random_severity}")
print("--------------------------------------------")
print(f"LOG SUMMARY ({entry_length} entries):")
print(incident_log[0])
print(incident_log[1])
print(incident_log[2])
print(incident_log[3])
print(incident_log[4])
print("--------------------------------------------")
print("             SIMULATION COMPLETE            ")
print("============================================")