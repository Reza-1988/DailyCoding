import tkinter as tk
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# FIND PASSWORD
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email_username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:\n{email}\nPassword:\n{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# SAVE PASSWORD
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
        'email_username': email_username,
        'password': password,
        }
    }

    if website == "" or password == "":
        messagebox.showerror(title="OoOops", message="Please fill all fields")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail:{email_username}"
                                                              f"\nPassword:{password}")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    # Making json file if is not exist
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    # Saving update data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)



# UI SETUP
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')


canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_image = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:", bg='white', fg='black')
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=21, bg='white', fg='black')
website_entry.grid(row=1, column=1)
website_entry.focus()

website_button = tk.Button(width=14,text="Search", bg='white', fg='black', command=find_password)
website_button.grid(row=1, column=2)

email_username_label = tk.Label(text="Email/Username:", bg='white', fg='black')
email_username_label.grid(row=2, column=0)

email_username_entry = tk.Entry(width=38, bg='white', fg='black')
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "Reza-1988@git.com")

password_label = tk.Label(text="Password:", bg='white', fg='black')
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=21, bg='white', fg='black')
password_entry.grid(row=3, column=1)

password_button = tk.Button(width=14, text="Generate Password", bg='white', fg='black', command=generate_password)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, bg='white', fg='black', command=save)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()