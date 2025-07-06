from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    if website_input == "" or email_input == "" or password_input == "":
        messagebox.showerror(title="Error", message="All fields are required")
    else:

        if "@" in email_input:

            is_okay = messagebox.askokcancel(
                title=website_input,
                message=f"There are the details entered;\n{website_input} | {email_input} | {password_input}\nIs it okay to save?",
            )

            if is_okay:

                with open(f"password_list.txt", mode="a") as file:
                    file.write(f"\n{website_input} | {email_input} | {password_input}")
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
        else:
            messagebox.showerror(title="Error", message="Valid email is required")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()

website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

# Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, "dummy_email@provider.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W")

gen_password_button = Button(text="Generate Password", command=gen_password)
gen_password_button.grid(column=2, row=3, sticky="EW")

# Add
add_button = Button(text="Add", width=35, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
