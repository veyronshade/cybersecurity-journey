# TEST 1 - CONSOLE OUTPUT (DAY 1)
print("================================================")
print("                ACCESS GRANTED                 ")
print("================================================")
print("Usename : admin")
print("Status  : Logged In")
print("================================================")

# TEST 2 - VARIABLES AND INPUT (DAY 1)
firstname = input("What is your first  name?\n")
lastname = input("What is your last name?\n")
age = int(input("How old are you?\n"))

print(f"Welcome {firstname} {lastname}!")
print(f"You are {age} years old.")

# TEST 3 - STRINGS MANIPULATION (DAY 1)
programming_languages = input("Enter your favorite programming languages: ")
length = len(programming_languages)
print(f"{programming_languages} has {length} letters.")

# Test 4 - Data Types (Day 2)
current_year = int(input("What is the current year? \n"))
d_o_b = int(input("What is your year of birth? \n"))
exact_year_age = current_year - d_o_b
print(f"You are {exact_year_age} years old")

# TEST 5 - Mathematical Operation (Day 2)
length2 = int(input("Input Lenght: \n"))
width = int(input("Input Width: \n"))
area = length2 * width
perimeter = length2 + width

print(f"Area is; {area}")
print(f"Perimeter is; {perimeter}")

# Test 6 -  f-string
name = input("What is your name?\n")
favourite_languages = input("Enter your favorite programming languages: ")
Years_of_experiences = input("How many years of experiences do you have?\n")

print(f"{name} has working with {favourite_languages} for {Years_of_experiences} years")

#  Test 7 - if/else (Day 3)
password = input("Input your password: ")
if password == "python123":
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

# Test 8 - Modulo (Day 3)
number = int(input("Type in your Number: "))
modulo = number % 2

if modulo == 0:
    print("Even Number")
else:
    print("Odd Number")

# Test 9 - BMI Interpretation
weight = float(input("What is your weight?\n"))
height = float(input("What is your height?\n"))
bmi = weight / (height**2)
print(bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You have an Normal weight")
elif bmi >= 25.0 and bmi <= 29.9:
    print("Damn boy!! You thick (Overweight)")
elif bmi >= 30:
    print("Forget about summer and move to the gym bro. You\'re OBESE")

#Test 9 -  Pizza CODE
print("Welcome to Pizza Code")
pizza_size = input("What pizza size would you like to get? S for Small, M for Medium, and L for Large ").lower()
toppings = input("What toppings do you desire on your pizza? N for Nigeria peppery suya, and D for dodo ").lower()
extra_cheese = input("Would you like extra cheese on your pizza? Y for yes and N for no ").lower()
bill = 0


if pizza_size == "s":
    bill += 10
    if toppings == "n":
        bill += 2
    elif toppings == "d":
        bill += 1
    else:
        bill += 0
elif pizza_size == "m":
    bill += 15
    if toppings == "n":
        bill += 2
    elif toppings == "d":
        bill += 1
    else:
        bill += 0
elif pizza_size == "l":
    bill += 20
    if toppings == "n":
        bill += 2
    elif toppings == "d":
        bill += 1
    else:
        bill += 0
else:
    print("Wrong Input!!")

if extra_cheese == "y":
    bill += 5
else:
    bill += 0
print(f"Your final bill is {bill}")

# Test 11 - Mini Adventure game

print('''
 ---.----.__..----.----| _|_||___||___||___||___||___||___||_|_ |
    |        |    |    | -.-..---..---..---..---..---..---..-.- |--.-
 ---'--.-----'----'--.-|  | ||   ||   ||   ||   ||   ||   || |  | `|
       |:           (| |  | ||   ||   ||   ||   ||   ||   || |  |--'-
       |:.           | | _|_||___||___||___||___||___||___||_|_ |
 ------'----.-.,----.'-| -.-..---..---..---..---..---..---..-.- |-.--
        ,/) |       |  |  | ||   ||   ||   ||   ||   ||   || |  | |`
 ----.---8--'--.----'--|  | ||   ||   ||   ||   ||   ||   || |  | |
     |   8     |:      | _|_||___||___||___||___||___||___||_|_ |-'--
     | ,)//    |:.     | -.-..---..---..---..---..---..---..-.- |:.
 ----'-`=;'--.-'-.----.|  | ||   ||   ||   ||   ||   ||   || |  |--.-
       //   /_ _( \    |  | ||   ||   ||   ||   ||   ||   || |  | /|
 ---.-//----)/\,'_/----| _|_||___||___||___||___||___||___||_|_ | `|
    |/|     `;=.(      | -.-..---..---..---..---..---..---..-.- |--'-
 (  |`.`.   |`,-/      |,-'-||---||---||---||---||---||---||-'-.|
 -`-'-.`.`-.';'=`.-..--'-.--------.-------------.--.-------.----'--.-
      |  `-./.}{-'\.)    |        )             |   `)     |       \
      |    :`-}{-''||    |:.      |   ,_        |          |:.     |
 ---'`'-.--|`-}{-'||)----'-.------'--'.,`--.----'--------.-'-------'-
        |  :`-`'-'/)|      |               |:.           |
 -.-----'--;`.}{,`.||----,-'--------.------'---.--------,'--.,-------
  |:     ,'/.`..'_(/(    |:         |          |             \
  |:.  ,',' |`--`.('))   |:.        |          |             |:
 -'--,' <.._|__,. >`,----'----------'--------.,'-------------'-------
     ``----....(','
            _,'>'
            )/
            `'
''')

prison= input("You have been wrongfully imprisoned locked away for thousand of years. Type \"Esc\" to escape or \"Stay\" to stay\n").lower()
choice = input("You have succesfully escaped. Type \"Revenge\" to take your revenge or \"Freedom\" to enjoy your freedom\n")
bomb = input("You are about to execute your enemies because they are all gathered in a meeting hall.\n Type \"Explode\" to destroy your enemies or \"Pistol\" to shoot your enemies while looking at their faces")

if prison == "esc":
    print("Escape in Progress...........")
    if choice == "revenge":
        print("Revenge Mapping in Progress...............")
    elif choice == "freedom":
        print("You are enjoying your freedom in italy")
    else:
        print("Game Over!! Wrong Input")
    if bomb == "explode":
        print("Your enemies have been blown to smithereens")
    elif bomb == "pistol":
        print("As the idiot that you are, you got shoot at the back of your by a guard")
    else:
        print("Game Over!! Wrong Input")
elif prison == "stay":
    print("Game Over!! You died in prison")
else:
    print("Game Over!! Wrong input")


# Test 12 - Password strength checker
passcode = input("Type in your pasword for strength checking: ")

if len(passcode) < 8:
    print("Password length is short and weak.")
else:
    print("Welldone. Password is strong")

# Bonus challenge
username = input("Username:\n")
password = input("Password:\n")

if username == "Veyron Shade" and password =="Python":
    print("ACCESS GRANTED")
elif username != "Veyron Shade" and password != "Python":
    print("Who are you🙄?? I don't know who you are😤!!")
elif username != "Veyron Shade":
    print("Unknown User")
elif password != "Python":
    print("Incorrect Password")

