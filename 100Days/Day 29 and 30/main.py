import json
from tkinter import *
from tkinter import messagebox
import random






# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for item in range(nr_letters)]
    numbers_list = [random.choice(numbers) for item in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for item in range(nr_symbols)]
    password_list = letter_list + numbers_list + symbols_list

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    page = website_entry.get()
    mail = email_entry.get()
    password = password_entry.get()
    new_data = {page: {
        'Email': mail,
        'Password': password
    }}

    if len(page) == 0 or len(password) == 0:
        messagebox.showinfo('Oops!', message='You left some values empty')
    else:
        try:
            with open('password.json', mode='r') as passwords:
                data = json.load(passwords)
        except FileNotFoundError:
            with open('password.json', mode='w') as passwords:
                json.dump(new_data, passwords, indent=4)
                # data.update(new_data)
        else:
            data.update(new_data)
            with open('password.json', mode='w') as passwords:
                json.dump(data, passwords, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Find Password SETUP ------------------------------- #
def find_password():
    website = website_entry.get()
    with open('password.json') as data_file:
        data = json.load(data_file)
    if website in data:
        print('hello world')
        email = data[website]['Email']
        password = data[website]['Password']
        messagebox.showinfo(title='Email', message=f'Email: {email}\n Passoword: {password}')
    else:
        print('hello')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Entries
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1, columnspan=1, sticky="W")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, sticky="W")

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, 'lalonunez@gmail.com')

# Labels
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Buttons
password_button = Button(text="Generate Password", width=15, command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_password = Button(text='Search', command=find_password)
search_password.grid(column=2, row=1, sticky="EW")

window.mainloop()
