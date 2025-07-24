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