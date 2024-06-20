import tkinter.messagebox
from tkinter import *
import random
from data_characters import characters_dict
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = [characters_dict[random.randint(1, 53)] for k in range(12)]
    positions_available = [x for x in range(len(password))]

    for i in range(2):
        choose_number = random.randint(53, 62)
        choose_position = random.choice(positions_available)
        number = characters_dict[choose_number]
        password[choose_position] = number
        positions_available.remove(choose_position)

    for i in range(2):
        choose_symbol = random.randint(63, 71)
        choose_position = random.choice(positions_available)
        symbol = characters_dict[choose_symbol]
        password[choose_position] = symbol
        positions_available.remove(choose_position)

    string_pass = ""
    for ch in password:
        string_pass += ch

    password_input.insert(0, string_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_input.get().lower()
    email_usern = email_input.get().lower()
    password = password_input.get().lower()

    new_data = {website:{
        "email": email_usern,
        "password": password,
    }}

    if website and email_usern and password:
        tkinter.messagebox.showinfo(title="Status", message="Data Submitted")
        try:
            with open("passwords.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("passwords.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

    else:
        tkinter.messagebox.showwarning(title="Status", message="Error, please fill in all fields")


# ---------------------------- Search Password ------------------------------- #

def search_password():
    with open("passwords.json", 'r') as data_file:
        data_dict = json.load(data_file)

    website = website_input.get().lower()

    try:
        tkinter.messagebox.showinfo(title="Your Info", message=f"email: {data_dict[website]["email"]}\npassword:{data_dict[website]["password"]}")
    except KeyError:
        tkinter.messagebox.showinfo(title="Your Info",
                                    message=f"You dont have any information for that site")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.configure(background='white', padx=20, pady=20)

canvas = Canvas(width=210, height=189, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)

website_text = Label(text="Website:", font=("arial", 11), bg="white")
website_text.grid(column=0, row=3)

website_input = Entry(width=46)
website_input.grid(column=1, row=3, columnspan=1)

email_text = Label(text="Email/Username:", font=("arial", 11), bg="white")
email_text.grid(column=0, row=4)

email_input = Entry(width=46)
email_input.grid(column=1, row=4, columnspan=1)

password_text = Label(text="Password:", font=("arial", 11), bg="white")
password_text.grid(column=0, row=5)

password_input = Entry(width=46)
password_input.grid(column=1, row=5, columnspan=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text="Search", command=search_password, width=14)
search_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", command=add_password, width=20, height=1)
add_button.grid(column=1, row=7, columnspan=2)

window.mainloop()
