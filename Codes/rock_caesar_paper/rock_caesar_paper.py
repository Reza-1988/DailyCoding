import random
from art import *


game_picture  = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor.\n= "))
computer_choice = random.randint(0,2)
if 0<=your_choice<=2:
    print(f"You're choice is: {game_picture[your_choice]}")
    print(f"Computer choice is: {game_picture[computer_choice]}")

    if your_choice == 0:
        if computer_choice == 2:
            print("You win!")
        elif computer_choice == 1:
            print("You lose!")
        else:
            print("It's draw!")

    elif your_choice == 1:
        if computer_choice == 2:
            print("You lose!")
        elif computer_choice == 0:
            print("You win!")
        else:
            print("It's draw!")
    elif your_choice == 2:
        if computer_choice == 1:
            print("You win!")
        elif computer_choice == 0:
            print("You lose!")
        else:
            print("It's draw!")

else:
    print("Pleas type 0 for Rock, 1 for Paper, 2 for Scissor.")