# ============================================================
# Question 3: Suspicious Activity Alert System
# Assessment: Python Technical Test
# Concepts Used: input(), int(), f-strings, arithmetic operators
# Date Completed: 2026-06-03
# ============================================================

username = input("Enter the flagged username: ")
ip_address = input("Enter the source IP address: ")
system_name = input("Enter the target system name: ")
failed_attempts = int(input("Enter number of failed login attempts: "))
alert_priority = int(input("Enter alert priority (1-5): "))
risk_score = failed_attempts * alert_priority

print("[!!!] SUSPICIOUS ACTIVITY ALERT [!!!]")
print(f"Username            : {username}")
print(f"Source IP           : {ip_address}")
print(f"Target System       : {system_name}")
print(f"Failed Attempts     : {failed_attempts}")
print(f"Alert Priority      : {alert_priority}/5")
print(f"Risk Score          : {risk_score}")
print("Action               : Flagged for analyst review")