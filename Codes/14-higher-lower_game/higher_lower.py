import random
from game_data import data
from art import logo, vs


def format_data(account):
    """Take the account data and return account information in printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from{country}"


def check_answer(user_guess, a_followers, b_followers):
    """Get user guess and followers and check if they got it right or wrong."""
    if user_guess == "a" and a_followers > b_followers:
        return True
    elif user_guess == "b" and a_followers < b_followers:
        return True
    else:
        return False


print(logo)
should_continue = True
current_score = 0
account_b = random.choice(data)

while should_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    followers_a_count = account_a['follower_count']
    followers_b_count = account_b['follower_count']

    is_correct = check_answer(guess, followers_a_count, followers_b_count)
    if is_correct:
        current_score += 1
        print(f"You got it! Current score: {current_score}.")
    else:
        print(f"Sorry, that's wrong! Final score: {current_score}.")
        should_continue = False

