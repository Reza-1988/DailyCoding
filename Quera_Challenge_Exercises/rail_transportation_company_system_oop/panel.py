import re
import string
import random
import os
from datetime import datetime


class Panel:
    employees = list()
    lines = dict()
    trains = dict()
    users = list()
    _admin_username = "Admin_Train"
    _admin_password = "Pass_Train"

    def __init__(self) -> None:
        self.id = self.generate_random_id(12)
        self.main_menu()

    def main_menu(self):
        print("--- Main Menu ---")
        print("1. Admin Login")
        print("2. Train Employee Login")
        print("3. User Registration")
        print("4. User Login")
        print("5. Exit")

        choice = self.get_choice(1, 5)
        if choice == 1:
            self.admin_login()
        elif choice == 2:
            self.train_employee_login()
        elif choice == 3:
            self.user_menu()
        elif choice == 4:
            self.user_login()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.match(pattern, email):
            return True
        else:
            return False

    def validate_password(self, password):
        if len(password) < 6:
            return False

        has_letter = re.search(r'[a-zA-Z]', password)
        has_digit = re.search(r'\d', password)
        has_special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

        return has_letter is not None and has_digit is not None and has_special_char is not None

    def admin_login(self):
        print("--- Admin Login ---")
        print("1. Login")
        print("0. Back")
        choice = self.get_choice(0, 1)
        if choice == 0:
            self.main_menu()
        elif choice == 1:
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if username == Panel._admin_username and password == Panel._admin_password:
                print("Admin logged in successfully!")
                self.admin_panel()
            else:
                print("Invalid username or password. Please try again.")

    def admin_panel(self):
        print("--- Admin Panel ---")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employee List")
        print("4. Logout")

        choice = self.get_choice(1, 4)
        if choice == 1:
            self.add_employee()
        elif choice == 2:
            self.remove_employee()
        elif choice == 3:
            self.view_employees()
        elif choice == 4:
            self.main_menu()
        else:
            print("Invalid choice. Please try again.")

    def add_employee(self):
        print("--- Add Employee ---")
        print("1. Add")
        print("0. Back")
        choice = self.get_choice(0, 1)
        if choice == 0:
            self.admin_panel()
        elif choice == 1:
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()
            email = input("Enter email: ")

            while not self.validate_email(email):
                print("Invalid email! Please try again.")
                email = input("Enter email: ").strip()

            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            while not self.validate_password(password):
                print("Password must include letters, digits, and '@' or '&'. Please try again.")
                password = input("Enter password: ").strip()

            employee = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "username": username,
                "password": password
            }
            Panel.employees.append(employee)
            print(f"Employee {first_name} {last_name} added successfully!")
            self.admin_panel()

    def remove_employee(self):
        print("--- Remove Employee ---")
        print("1. remove")
        print("0. Back")
        choice = self.get_choice(0, 1)
        if choice == 0:
            self.admin_panel()
        elif choice == 1:
            print(f"Usernames are: {Panel.employees}")
            username = input('Enter the username of the employee to remove: ').strip()

            for idx, emp in enumerate(Panel.employees):
                if emp["username"] == username:
                    del Panel.employees[idx]
                    print(f"Employee with username '{username}' removed")
                    break

                else:
                    print('The username does not exist! Please try again')
            self.admin_panel()

    def view_employees(self):
        print("--- View Employee List ---")
        print("1. View Employees")
        print("0. Back")
        choice = self.get_choice(0, 1)
        if choice == 0:
            self.admin_panel()
        elif choice == 1:
            if not Panel.employees:
                print("There are no employees")
            else:
                print('List of Employees:')
                for emp in Panel.employees:
                    print(
                        f'Username: {emp["username"]}, First Name: {emp["first_name"]}, Last Name: {emp["last_name"]}, Email: {emp["email"]}, Password: {emp["password"]}\n')
            self.admin_panel()

    def train_employee_login(self):
        print("--- Train Employee Login ---")
        print("0. Back")
        print("1. Login")
        choice = self.get_choice(0, 1)
        if choice == 0:
            self.main_menu()
        elif choice == 1:
            while True:
                username = input("Enter employee username: ").strip()
                password = input("Enter employee password: ").strip()

                found = False
                for emp in Panel.employees:
                    if emp['username'] == username and emp['password'] == password:
                        print('Employee logged in successfully!')
                        found = True
                        self.employee()
                        break
                if not found:
                    print('The username or password is Incorrect!')
                else:
                    break

    def employee(self):
        print("--- Train Employee Panel ---")
        print("1. Add Line")
        print("2. Update Line")
        print("3. Delete Line")
        print("4. View Lines")
        print("5. Add Train")
        print("6. Delete Train")
        print("7. View Trains")
        print("8. Logout")

        number_choice = self.get_choice(1, 8)
        if number_choice == 1:
            self.add_line()
        elif number_choice == 2:
            self.update_line()
        elif number_choice == 3:
            self.delete_line()
        elif number_choice == 4:
            self.view_lines()
        elif number_choice == 5:
            self.add_train()
        elif number_choice == 6:
            self.delete_train()
        elif number_choice == 7:
            self.view_trains()
        elif number_choice == 8:
            print("Logging out...")
            self.main_menu()

    def get_choice(self, min_, max_):
        while True:
            try:
                choice = int(input(f"Please enter a number between {min_} and {max_}: "))
                if choice in range(min_, max_ + 1):
                    return choice
            except ValueError:
                print(f"Invalid input, please enter a number between{min_} and {max_}")

    def add_line(self):
        print("--- Add Line ---")
        line_name = input("Enter line name: ").strip()
        if line_name in Panel.lines:
            print("Line already exists. Please enter a unique name.")
        else:
            start_point = input("Enter start location: ").strip()
            end_point = input("Enter destination: ").strip()
            train_number = input("Enter train number: ").strip()
            stations = input("Enter station names (please separate names with comma): ").strip().split(",")
            Panel.lines[line_name] = [start_point, end_point, train_number, stations]
            print(f"Line '{line_name}' added successfully.")
        self.employee()

    def update_line(self):
        if not Panel.lines:
            print("No lines available to update.")
            self.employee()
            return

        print("--- Update Line ---")
        while True:
            print("Available lines:", list(Panel.lines.keys()))
            line_name = input("Enter the line name to update: ").strip()
            if line_name in Panel.lines:
                start_point, end_point, train_number, stations = Panel.lines[line_name]
                print(f"Current details: \nStart Point: {start_point} \nEnd Point: {end_point} \nStations: {stations}")
                print("1. Update Start Point")
                print("2. Update End Point")
                print("3. Update Stations Names")
                number_field = self.get_choice(1, 3)
                if number_field == 1:
                    new_start_point = input("Enter new start location: ").strip()
                    Panel.lines[line_name][0] = new_start_point
                elif number_field == 2:
                    new_end_point = input("Enter new end location: ").strip()
                    Panel.lines[line_name][1] = new_end_point
                elif number_field == 3:
                    new_stations = input("Enter new stations (comma-separated): ").strip().split(",")
                    Panel.lines[line_name][2] = new_stations
                print(f"Line '{line_name}' updated successfully.")
                break
            else:
                print("Invalid line name. Please try again.")
        self.employee()

        def delete_line(self):
            if len(Panel.lines) == 0:
                print("No lines available to delete.")
                self.employee()
                return

            print("--- Delete Line ---")
            while True:
                print("Available lines:", list(Panel.lines.keys()))
                line_name = input("Enter the line name to delete: ").strip()
                if line_name in Panel.lines:
                    del Panel.lines[line_name]
                    print(f"Line '{line_name}' deleted successfully.")
                    break
                else:
                    print(f"Line '{line_name}' does not exist. Please try again.")
            self.employee()

        def delete_train(self):
            if len(Panel.lines) == 0:
                print("No trains available to delete.")
                self.employee()
                return
            print("--- Delete Train ---")
            while True:
                print("Available trains:", list(Panel.trains.keys()))
                train_id = input("Enter the train ID to delete: ").strip()
                if train_id in Panel.trains:
                    del Panel.trains[train_id]
                    print(f"Train with ID: {train_id}, deleted successfully.")
                    break
                else:
                    print(f"Train with ID: {train_id}, does not exist. Please try again.")
            self.employee()

        def view_trains(self):
            if len(Panel.trains) == 0:
                print("No trains available.")
            else:
                print("\n--- List of Trains ---")
                for train_id, details in Panel.trains.items():
                    print(f"Train ID: {train_id} \nName: {details[0]} \nLine: {details[1]} \nSpeed: {details[2]} "
                          f" \nStop Time: {details[3]} \nQuality: {details[4]} \nTicket: {details[5]} \nCapacity: {details[6]}")
                self.employee()

        def user_menu(self):
            print("--- User Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Return To Main Menu")
            print(Panel.users)

            choice = self.get_choice(1, 3)
            if choice == 1:
                self.user_register()
            elif choice == 2:
                self.user_login()
            elif choice == 3:
                print("going back to main menu")
                self.main_menu()

        def user_register(self):
            print("--- User Registration ---")
            already_exists = False
            while True:
                email = input("Enter email: ").strip()
                if self.validate_email(email=email) is False:
                    print("Enter email again correctly")
                    continue

                for user in Panel.users:
                    if user["email"] == email:
                        print("Email already taken, enter new email")
                        already_exists = True
                if already_exists:
                    continue
                break
            while True:
                username = input("Enter username: ").strip()
                for user in Panel.users:
                    already_exists = False
                    if user["username"] == username:
                        print("username already taken, enter new email")
                        already_exists = True
                if already_exists:
                    continue
                break
            while True:
                password = input("Enter password: ").strip()
                if self.validate_password(password=password) is False:
                    print("enter password again correctly")
                    continue
                break
            self.user(username, password, email)
            self.user_menu()

        def user_login(self):
            print("--- User Login ---")
            while True:
                username = input("enter username: ").strip()
                password = input("enter password: ").strip()
                is_correct = False
                for user in Panel.users:
                    if user["username"] == username:
                        if user["password"] == password:
                            print("username or password is wrong. enter again")
                            is_correct = True
                if is_correct:
                    print("you entered successfully. you can go ...")
                    self.panel_purchase(username)
                    break
                else:
                    continue

        def user(self, username, password, email):

            wallet_amount = int(''.join(str(random.randint(1, 9)) for _ in range(6)))
            user = dict(username=username, password=password, email=email, wallet=wallet_amount)
            Panel.users.append(user)
            print("registration completed. you can login now!")

        def generate_random_id(self, length=8):
            characters = string.ascii_letters + string.digits  # Include letters and digits
            random_id = ''.join(random.choice(characters) for _ in range(length))
            return random_id

        def panel_purchase(self, username):
            print("--- Purchase Panel ---")
            print("1. Menu Buy ticket")
            print("2. Change account information")
            print("3. Exit")
            option = self.get_choice(min_=1, max_=3)

            if option == 1:
                self.menu_buy_ticket(username)
            elif option == 2:
                self.menu_change_account_information()
            elif option == 3:
                print("Logging out...")
                self.user_menu()

        def menu_buy_ticket(self, username):
            print("--- Buy Ticket Menu ---")
            print("1. View Trains")
            print("2. Add Funds to Wallet")
            print("3. Buy Ticket")
            print("4. View Recent Transactions")
            print("5. Logout")
            option = self.get_choice(min_=1, max_=5)
            if option == 1:
                self.view_trains()
            elif option == 2:
                self.add_funds(username)
            elif option == 3:
                self.buy_ticket(username)
            elif option == 4:
                self.view_transactions(username)
            elif option == 5:
                print("Logging out...")
                self.user_menu()

        def add_funds(self, username):
            api = API()
            while True:
                try:
                    amount = float(input("Enter the amount to add to your wallet: ").strip())
                    card = int(input("enter your card number: ").strip())
                    exp_year = int(input("enter your exp year: ").strip())
                    exp_month = int(input("enter your exp month: ").strip())
                    password = int(input("enter your card password: ").strip())
                    cvv2 = int(input("enter your cvv2: ").strip())
                except ValueError as e:
                    print(f'Error :{e}')
                    continue
                if amount <= 0:
                    print("Amount must be positive.")
                    continue

                if not api.validate(card, exp_month, exp_year, password, cvv2):
                    print(f'somthing is wrong\n{card}\n{exp_year}\n{exp_month}\n{password}\n{cvv2}')
                    continue
                api.pay(card, exp_month, exp_year, password, cvv2, amount)
                for user in Panel.users:
                    if user['username'] == username:
                        user['wallet'] += amount

        def buy_ticket(self, username):
            train_id = input("Enter the Train ID you want to buy a ticket for: ").strip()
            print("Choose amount of ticket between 1 to 10: ")
            quantity = self.get_choice(min_=1, max_=10)  # TODO
            for user in Panel.users:  # TODO
                if user['username'] == username:
                    if train_id in Panel.trains.keys():
                        train = Panel.trains[train_id]
                        total_price = int(train[5]) * quantity

                        user_wallet = user['wallet']
                        if user_wallet >= total_price:
                            if int(train[-1]) >= quantity:
                                train[-1] = int(train[-1]) - quantity
                                user['wallet'] -= total_price

                                print("Ticket purchased successfully!")
                            else:
                                print("Not enough capacity available.")
                        else:
                            print("Insufficient funds in wallet.")
                    else:
                        print("Invalid Train ID. Please try again.")
            self.menu_buy_ticket(username)

        def view_transactions(self, username):  # TODO
            try:
                with open(f"{username}_transactions.txt", "r") as file:
                    transactions = file.readlines()
                    if transactions:
                        print("--- Recent Transactions ---")
                        for transaction in transactions:
                            print(transaction.strip())
                    else:
                        print("No recent transactions.")
            except IOError as error:
                print(f"No such file, {error}")

        def record_transaction(self, amount, transaction_type, train_id=None, quantity=None, username=None):  # TODO
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            file_name = f"{username}_transactions.txt"
            try:
                with open(file_name, "a") as file:
                    transaction = f"{current_time} - {transaction_type}: Amount: {amount}, Train ID: {train_id if train_id else 'N/A'}, Quantity: {quantity if quantity else 'N/A'}\n"
                    file.write(transaction)
            except IOError as error:
                print(f'IOError : {error}')
                return
            print(f"Transaction recorded for {username} in {file_name}")

        def menu_change_account_information(self):  # TODO
            while True:
                found = False
                username = input('Enter your username: ').strip()
                for user in Panel.users:
                    if user['username'] == username:
                        email = user['email']
                        password = user['password']
                        found = True
                if found:
                    break

            print(f"--- Account Information ---")
            print("0. Return")
            print(f"1. Username: {username}")
            print(f"2. Email: {email}")
            print(f"3. Password: ****")

            option = self.get_choice(min_=0, max_=3)
            if option == "0":
                self.panel_purchase(username)
            elif option == "1":
                print("You can't change your username.")
            elif option == "2":
                self.change_email(email=email)
            elif option == "3":
                self.change_password(password)

        def change_email(self, old_email):  # TODO
            while True:
                print("Enter your new email (or * to return): ")
                new_email = input().strip()
                if new_email == "*":
                    self.menu_change_account_information()
                    return
                elif self.validate_email(new_email):
                    for user in Panel.users:
                        if old_email == user['email']:
                            user['email'] = new_email
                    print(f"Email changed to {new_email}")
                    self.menu_change_account_information()
                    return
                else:
                    print("Please enter a correct email!")

        def change_password(self, old_password):
            while True:
                new_password = input("Enter new password (or 0 to return): ").strip()
                if new_password == "0":
                    self.menu_change_account_information()
                    return
                elif self.validate_password(new_password):
                    confirm_password = input("Confirm new password (or 0 to return): ").strip()
                    if confirm_password == "0":
                        self.menu_change_account_information()
                        return
                    elif new_password == confirm_password:
                        for user in Panel.users:
                            if user['password'] == old_password:
                                user['password'] = new_password
                        print("Password changed successfully!")
                        self.menu_change_account_information()
                        return
                    else:
                        print("Passwords do not match, try again!")
                        continue
                else:
                    print("Enter a valid password!")

        def validate_date(self, date):
            pattern = r'^\d{4}-\d{2}-\d{2}$'
            return re.match(pattern, date) is not None
