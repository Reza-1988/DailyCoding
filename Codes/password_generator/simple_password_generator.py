import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Random password with repeated characters
password_list_with_repetition_char = list()
for char in range(0, nr_letters):
    password_list_with_repetition_char.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list_with_repetition_char.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list_with_repetition_char.append(random.choice(numbers))
random.shuffle(password_list_with_repetition_char)
password_1 = ""
for item in password_list_with_repetition_char:
    password_1 += item
print(f"Your random password with repeated characters is: {password_1}")


# Random password with unique characters also (way 2) with random.sample module
password_list_with_unique_char = list()
password_list_with_unique_char.extend(random.sample(letters, nr_letters ))
password_list_with_unique_char.extend(random.sample(numbers, nr_numbers ))
password_list_with_unique_char.extend(random.sample(symbols, nr_symbols ))
random.shuffle(password_list_with_unique_char)

password_2 = ""
for item in password_list_with_unique_char:
    password_2 += item
print(f"Your random password with unique characters is: {password_2}")
