from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD -------------------------------

file = open('Data', 'a')
def add_data():
    file.write(f'{website} ! {username} ! {password}')
    

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
generate_password = Button(text='Generate Password', width=20)
generate_password.grid(row=4, column=2)

website = website_entry.get()
username = username_entry.get()
password = password_entry.get()

add_button = Button(text="Add", width=45, command=add_data)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
