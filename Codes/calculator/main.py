import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error division by zero"
    else:
        return n1 / n2

operations = {
    "+": add, "-": subtract, "*": multiply, "/": divide,
}

def calculator():
    print(art.logo)
    should_continue = True
    first_number = float(input("Enter first number: "))
    while should_continue:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("Enter second number: "))
        result = operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        choose = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choose == "y":
            first_number = result
            should_continue = True
        elif choose == "n":
            should_continue = False
            print("\n" * 100)
            calculator()

calculator()