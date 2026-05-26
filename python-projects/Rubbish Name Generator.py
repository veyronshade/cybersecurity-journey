# Day 1 Project: Rubbish Name Generator
# Concepts practiced: input(), string indexing, string concatenation
# Part of my Python learning journey for Ethical Hacking

# HOW TO RUN:
# python3 "Rubbish Name Generator.py"
# (Requires Python 3 — no external libraries needed)

print("Welcome to the Rubbish Name Generator")
first_name = input("What's your name?\n")

second_name = input("What's the name of something you really love doing?\n")

print("You are " + first_name + " and You Love " + second_name)
print("Hurray!!! Your Rubbish Name is ready")
input("Type Yes to get the result\n")
result = first_name[2] + second_name[1] + first_name[3] + second_name[4]
print("Your rubbish name is " + result + " 😂.")
