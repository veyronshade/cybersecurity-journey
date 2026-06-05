import random

# REFACTORED VERSION BELOW

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# REFACTORED VERSION BELOW
# REFACTORED VERSION BELOW
# your_choice = input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
#
# if your_choice == "0":
#     print(rock)
#     print(f"Computer choose:")
#     computer_choice = [rock, paper, scissors]
#     hand_sign = random.choice(computer_choice)
#     print(hand_sign)
#
#     if hand_sign == paper:
#         print("You lose")
#     elif hand_sign == rock:
#         print("Stalemate")
#     else:
#         print ("You win")
# elif your_choice == "1":
#     print(paper)
#     print(f"Computer choose:")
#     computer_choice = [rock, paper, scissors]
#     hand_sign = random.choice(computer_choice)
#     print(hand_sign)
#     if hand_sign == scissors:
#         print("You lose")
#     elif hand_sign == rock:
#         print("You win")
#     else:
#         print ("Stalemate")
# elif your_choice == "2":
#     print(scissors)
#     print(f"Computer choose:")
#     computer_choice = [rock, paper, scissors]
#     hand_sign = random.choice(computer_choice)
#     print(hand_sign)
#     if hand_sign == rock:
#         print("You lose")
#     elif hand_sign == scissors:
#         print("Stalemate")
#     else:
#         print ("You win")
# REFACTORED VERSION BELOW


ascii_art = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >= 3 or player_choice < 0:
    print("You picked wrongly. You lose!")
else:
    print(ascii_art[player_choice])

    computer_choice = random.randint(0,2)
    print("Computer choose: ")
    print(ascii_art[computer_choice])

    if player_choice == computer_choice:
        print("It looks like we have a draw")
    elif player_choice == 0 and computer_choice == 2:
        print("Damn!! You lose!")
    elif player_choice == 2 and computer_choice == 0:
        print("Hurray!! You won!")
    elif player_choice > computer_choice:
        print("Hurray!! You won!")
    elif computer_choice > player_choice:
        print("Damn!! You lose!")