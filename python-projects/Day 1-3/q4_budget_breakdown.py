# ============================================================
# Question 4: Security Budget Breakdown Planner
# Assessment: CyberTech Solutions — Python Technical Test
# Concepts Used: input(), float(), int(), arithmetic operators, f-strings
# Date Completed: 2026-06-03
# ============================================================


annual = round(float(input("Enter total annual security budget (USD): ")), 2)
number_of_staff = int(input("Enter number of security staff: "))
percentage =  round(float(input("Enter % of budget for software tools: ")), 2)

quarterly_budget = round(annual / 4, 2)
software_budget = round((percentage / 100) * annual, 2)
staff_budget = round(annual - software_budget, 2)
budget_per_person = round(staff_budget / number_of_staff, 2)

print("===== SECURITY BUDGET BREAKDOWN =====")
print(f"Annual Budget           : ${annual}")
print(f"Quarterly Budget        : ${quarterly_budget}")
print(f"Software Application    : ${software_budget} ({percentage}%)")
print(f"Staff Budget            : ${staff_budget}")
print(f"Budget per Staff        : ${budget_per_person}")
print("=====================================")





