from coffee_machine_data import *


money = 0
is_on = True
def report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"


def update_resources(coffee):
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['milk'] -= MENU[coffee]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    return print("resources updated!")


def check_input_and_resource(coffee):
    """check the input and check are resources sufficient."""
    global is_on
    if order == "off":
        is_on = False
        return print("See you later!")
    elif coffee == "report":
        return print(report())
    elif resources['water'] >= MENU[coffee]['ingredients']['water']:
        if resources["milk"] >= MENU[coffee]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
                print(coffee)
                transaction(coffee)
            else:
                print("Sorry there is not enough coffee.")
                return
        else:
             print("Sorry there is not enough milk.")
        return
    else:
        print("Sorry there is not enough water.")
        return


def transaction(coffee):
    global money
    print(f"You're {coffee} cost is: {MENU[coffee]["cost"]}")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    calculate_coins = ((quarters * MONEY['quarters']) + (dimes * MONEY['dimes']) + (nickles * MONEY['nickles']) +
    (pennies * MONEY['pennies']))
    if calculate_coins >= MENU[coffee]["cost"]:
        money += calculate_coins
        print(f"Here is your change  ${round((calculate_coins - MENU[coffee]['cost']),2)}. Here is your {coffee} Enjoy ☕️")
        update_resources(coffee)
    else:
        print(f"Sorry that's not enough money. ${round(calculate_coins,2)} refunded.")
        return


while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    check_input_and_resource(order)
