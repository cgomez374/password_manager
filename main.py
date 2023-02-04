import tkinter
from pyperclip import copy
from tkinter import messagebox
from password_generator import generate_password


# PASSWORD GENERATOR

def add_generated_password():
    password_entry.delete(0, 'end')
    password_entry.insert(0, generate_password())
    copy(password_entry.get())
    messagebox.showinfo(title='Success', message='New password copied to clipboard!')


# SAVE PASSWORD


def save():
    ok_to_add = False

    website = website_name_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if website == '':
        messagebox.showerror(title='Error', message='Website empty!')
    elif email_username == '':
        messagebox.showerror(title='Error', message='Email/Username empty!')
    elif password == '':
        messagebox.showerror(title='Error', message='Password empty!')
    else:
        ok_to_add = messagebox.askokcancel(title=website.capitalize(), message=f'Email/Username: {email_username}\n'
                                                                f'Password: {password}'
                                                                f'\nPlease confirm details are correct before adding!')

    if ok_to_add:
        with open('./data.txt', 'a') as file:
            file.write(f'{website} | {email_username} | {password}\n')
        website_name_entry.delete(0, 'end')
        email_username_entry.delete(0, 'end')
        email_username_entry.insert(0, 'example@example.com')
        password_entry.delete(0, 'end')
        messagebox.showinfo(title='Success', message='Login details saved!')


# UI SETUP

# Window

window = tkinter.Tk()
window.title('Password Manager')
window.config(width=300, height=300, padx=50, pady=50, bg='white')

# Canvas for photo

logo_photo = tkinter.PhotoImage(file='./logo.png')
canvas = tkinter.Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=logo_photo)
canvas.grid(row=0, column=1, pady=(10, 10))

# Website Name Label

website_name_label = tkinter.Label(text='Website: ', bg='white')
website_name_label.grid(row=1, column=0, pady=(10, 10))

# Website Name Entry

website_name_entry = tkinter.Entry(width=35)
website_name_entry.grid(row=1, column=1, columnspan=2, pady=(10, 10))
website_name_entry.focus()

# Email/Username Name Label

email_username_label = tkinter.Label(text='Email/Username: ', bg='white')
email_username_label.grid(row=2, column=0, pady=(10, 10))

# Email/Username Name Entry

email_username_entry = tkinter.Entry(width=35)
email_username_entry.insert(0, 'example@example.com')
email_username_entry.grid(row=2, column=1, columnspan=2, pady=(10, 10))

# Password Name Label

password_label = tkinter.Label(text='Password: ', bg='white')
password_label.grid(row=3, column=0, pady=(10, 10))

# Password Name Entry

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, pady=(10, 10))

# Generate Password Button
# NEED TO FIX PADDING ----------------

generate_button = tkinter.Button(text='Generate Password', width=14, command=add_generated_password)
generate_button.grid(row=3, column=2, pady=(10, 10))

# Add Button

add_button = tkinter.Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=(10, 10))

# Required for window

window.mainloop()

