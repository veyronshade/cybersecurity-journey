# ============================================================
# Question 8: SOC Analyst Shift Pay Calculator
# Assessment: CyberTech Solutions — Python Technical Test
# Concepts Used: input(), int(), float(), if/elif/else, nested if, arithmetic operators, f-strings
# Date Completed:
# Status: In Progress
# ============================================================

analyst_name = input("Enter analyst name: ")
shift_start = int(input("Enter shift start hour (0-23): "))
shift_duration = int(input("Enter shift duration in hours: "))
grade_level = int(input("Enter pay grade (1,2 or 3): "))
incident_count = int(input("Enter number of incidents handled: "))

shift_end = shift_start + shift_duration

if grade_level == 1:
    rate = 15
elif grade_level == 2:
    rate = 22
elif grade_level == 3:
    rate = 35
else:
    print("Please input accurate grade")

base_pay = rate * shift_duration

overtime = 0
if shift_end >22:
    overtime = shift_end - 22
    regular_hours = shift_duration - overtime
    total_pay = (regular_hours * rate) + (overtime * rate * 1.5)
else:
    total_pay = rate * shift_duration

if overtime > 0:
    overtime = f"Yes — {overtime} hrs"
else:
    overtime = "No"


if incident_count > 10:
    bonus_percentage = 15
elif incident_count >= 6 and incident_count <= 10:
    bonus_percentage = 10
elif incident_count >=1 and incident_count <=5:
    bonus_percentage = 5
elif incident_count <= 0:
    bonus_percentage = 0
else:
    bonus_percentage = 0

bonus = total_pay * (bonus_percentage / 100)
final_payout = total_pay + bonus

print("===== SHIFT PAYMENT SUMMARY =====")
print(f"Analyst         : {analyst_name}")
print(f"Shift           : {shift_start}:00 - {shift_end}:00")
print(f"Duration        : {shift_duration} hours")
print(f"Pay Grade       : Level {grade_level} ${rate}/hr")
print("---------------------------------")
print(f"Base Pay        : ${base_pay}")
print(f"Overtime        : {overtime}")
print(f"Total Pay       : ${total_pay}")
print(f"Incidents       : {incident_count}")
print(f"Bonus           : ${bonus} {bonus_percentage}%")
print(f"FINAL PAYOUT    : ${final_payout}")
print("==================================")