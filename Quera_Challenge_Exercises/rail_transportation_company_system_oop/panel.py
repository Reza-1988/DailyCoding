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