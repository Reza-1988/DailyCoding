import random
import number_guessing_game_art

EASY_LEVEL =10
HARD_LEVEL = 5

def check_guess(guess, answer, attempts):
    if guess > answer:
        print("Too high\nGuess again!")
        return attempts - 1
    elif guess < answer:
        print("Too low\nGuess again!")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer} and you have {attempts} attempts left.")

def set_difficulty():
    level = input("Choose a difficulty. Type easy or hard: ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL

def game():
    print(art.logo)
    true_answer = random.randint(1, 100)
    user_guess = 0
    print("Welcome to Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    attempts = set_difficulty()

    while user_guess != true_answer:
        print(f"You have {attempts} attempts left.")
        user_guess = int(input("Make a guess: "))
        attempts = check_guess(user_guess, true_answer, attempts)
        if attempts == 0:
            print("Sorry, you lose.")
            break


game()