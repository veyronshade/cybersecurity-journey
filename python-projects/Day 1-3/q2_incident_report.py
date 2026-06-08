# ============================================================
# Question 2: Security Incident Report Intake
# Assessment: CyberTech Solutions — Python Technical Test
# Concepts Used: input(), f-strings, string concatenation
# Date Completed: 2026-06-03
# ============================================================


analyst_name = input("Enter analyst name: ")
incident_type = input("Enter incident type: ")
date = input("Enter date (DD/MM/YYYY): ")
time = str(input("Enter time of Detection (HH:MM): "))

print("------ INCIDENT REPORT HEADER ------")
print(f"Analyst     : {analyst_name}")
print(f"Type        : {incident_type}")
print(f"Date/Time   : {date} at {time}")
print(f"Reference   : INC-{analyst_name}-{date}")
print(f"Status      : OPEN - Pending Investigation")
print("------------------------------------")

