# ============================================================
# Question 5: Incident Threat Score Analyser
# Assessment: CyberTech Solutions — Python Technical Test
# Concepts Used: input(), int(), float(), arithmetic operators, round(), int() truncation, f-strings
# Date Completed: 2026-06-03
# ============================================================

systems = int(input("Enter number of affected systems: "))
sensitivity = int(input("Enter data sensitivity level (1-10): "))
hours = float(input("Enter hours since detection: "))

threat_score = (systems * sensitivity) + (hours * 2.5)
rounded_score = round(threat_score, 1)
truncated_score = int(threat_score)
threat_percentage = round((threat_score / 200) * 100, 1)

print("===== THREAT SCORE REPORT =====")
print(f"Systems Affected    : {systems}")
print(f"Sensitivity Level   : {sensitivity}/10")
print(f"Hours Since Alert   : {hours}")
print(f"-------------------------------")
print(f"Raw Threat Score    : {threat_score}")
print(f"Rounded Score       : {rounded_score}")
print(f"Truncated Score     : {truncated_score}")
print(f"Threat Percentage   : {threat_percentage}% of maximum (200)")