from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD -------------------------------

def add_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # if not website.isalnum() or not password.isalnum() or not username.isalnum():
    #     print('Yeah')
    # print("done")
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Missing Information', message='Some fields are empty!')

    else:

        is_ok = messagebox.askokcancel(title=website, message=f'Are these details correct? \n '
                                                              f'Email/Username:{username} \n Password: {password}  ')
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f'{website} ! {username} ! {password} \n')
                print('done')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(row=2, column=0)
website_entry = Entry(width=45)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=0)
username_entry = Entry(width=45)
username_entry.grid(row=3, column=1, columnspan=2)
username_entry.insert(0, 'elluhstephanie4good@gmail.com')

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=4, column=1)
generate_password = Button(text='Generate Password', width=20, command=generate_password)
generate_password.grid(row=4, column=2)

add_button = Button(text="Add", width=45, command=add_data)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
