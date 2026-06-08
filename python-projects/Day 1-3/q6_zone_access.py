# ============================================================
# Question 6: Security Zone Access Control
# Assessment: Python Technical Test
# Concepts Used: input(), int(), if/elif/else, nested if, logical operators (and, or)
# Date Completed: 2026-06-03
# ============================================================


name = input("Enter your name: ")
zone = input("Enter zone to access (A, B or C): ").upper()
if zone == "A":
    level = int(input("Enter clearance level (1,2 or 3): "))
    if level == 1 or level == 2 or level == 3:
        print("ACCESS GRANTED. You have been cleared")
    else:
        print("ACCESS DENIED. You haven't been assigned a level yet")

elif zone == "B":
    level = int(input("Enter clearance level (1, 2 or 3): "))
    if level == 2 or level == 3:
        hour = int(input("Enter current hour (0-23): "))
        if hour >= 7 and hour <= 19:
            print("ACCESS GRANTED. You have been cleared")
        else:
            print("ACCESS DENIED. Access to the server room at this time is not allowed")
    else:
        print("ACCESS DENIED. Requires Level 2 or 3 Clearance")

elif zone == "C":
    level = int(input("Enter clearance level (1, 2 or 3): "))
    if level == 3:
        hour = int(input("Enter current hour (0-23): "))
        if hour >= 9 and hour <= 17:
            print("ACCESS GRANTED. You have been cleared")
        else:
            print("ACCESS DENIED. Access to the server room at this time is not allowed")
    else:
        print("ACCESS DENIED. Requires Level 3 Clearance")

else:
    print("You are not cleared for access. You have not be assigned a level access tag")


