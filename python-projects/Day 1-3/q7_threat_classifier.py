# ============================================================
# Question 7: Incident Threat Level Classifier
# Assessment: CyberTech Solutions — Python Technical Test
# Concepts Used: input(), int(), float(), if/elif/else, logical operators (and, or), comparison operators
# Date Completed:
# ============================================================

systems_compromised = int(input("Enter number of systems compromised: "))
exposed = input("Is sensitive data exposed? (yes/no): ").lower()
hours = float(input("Enter hours since first detection: "))
if systems_compromised > 50 and exposed == "yes" and hours > 48:
    print("THREAT LEVEL: CATASTROPHIC - This requires urgent handling, Full SYSTEM COMPROMISE TOO LATE. "
          "Forensic Investigation Required Immediately")
elif systems_compromised > 50 and exposed =="yes":
    print("THREAT LEVEL: CRITICAL - Sensitive data is exposed, Forensic investigation is highly recommended.")
elif systems_compromised > 20 or (exposed =="yes" and hours > 24):
    print("THREAT LEVEL: HIGH - Sensitive data at risk of being exposure, handle this case with caution.")
elif systems_compromised > 5 and hours > 24:
    print("THREAT LEVEL: MEDIUM - Isolate compromised systems to prevent threat escalation ")
elif systems_compromised > 0:
    print("THREAT LEVEL: LOW - Compromised - Compromised system should be thoroughly checked")
else:
    print("CLEAR, THREAT LEVEL IS NONEXISTENT")