# ☕ Coffee Machine Program

This is a simple **Coffee Machine** program written in Python. It simulates a basic coffee vending machine, allowing users to order coffee, process payments, and track resources.

###  How It Works

- The program starts and continuously prompts the user to order a coffee (`espresso`, `latte`, or `cappuccino`).
- Users can type **"report"** to see the current resource status (water, milk, coffee, and money).
- If the user types **"off"**, the machine shuts down.
- The machine checks if there are enough ingredients for the selected coffee.
- If resources are sufficient, it asks for **coin input** (quarters, dimes, nickels, pennies).
- If enough money is provided, the transaction is processed, change is returned, and resources are updated.
- If not enough money is inserted, the amount is refunded.

##  Requirements

- Python 3.x
- `coffee_machine_data.py` file (containing `MENU`, `resources`, and `MONEY` dictionaries)

##  Features

- Orders **espresso, latte, or cappuccino**
- **Resource tracking** (water, milk, coffee)
- **Transaction system** (accepts quarters, dimes, nickels, and pennies)
- **Automatic resource update** after a successful purchase
- **Machine shutdown** with `"off"` command
- **Report generation** with `"report"` command

