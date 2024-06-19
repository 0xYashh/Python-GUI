from tkinter import *
from tkinter import messagebox
import pandas as pd
import os

# Function to save account data
def create_account():
    email = email_input.get()
    password = password_input.get()

    if email and password:
        if os.path.exists('users.csv'):
            df = pd.read_csv('users.csv')
        else:
            df = pd.DataFrame(columns=["Email", "Password"])
        
        if email in df['Email'].values:
            messagebox.showerror('Error', 'Email already exists')
        else:
            new_user = pd.DataFrame([[email, password]], columns=["Email", "Password"])
            df = pd.concat([df, new_user], ignore_index=True)
            df.to_csv('users.csv', index=False)
            messagebox.showinfo('Success', 'Account created successfully')
            email_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showerror('Error', 'Please fill in both fields')

# Function to handle login
def handle_login():
    email = email_input.get()
    password = password_input.get()

    if os.path.exists('users.csv'):
        df = pd.read_csv('users.csv')
        if ((df['Email'] == email) & (df['Password'] == password)).any():
            messagebox.showinfo('Login Status', 'Login successful')
        else:
            messagebox.showerror('Login Status', 'Invalid email or password')
    else:
        messagebox.showerror('Login Status', 'No accounts found. Please create an account first.')

# Root window
root = Tk()
root.title('Account Creation and Login')
root.geometry('350x450')
root.configure(bg='white')

# Email label and input
email_label = Label(root, text='Enter Email', fg='black', bg='white')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

# Password label and input
password_label = Label(root, text='Enter Password', fg='black', bg='white')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50, show='*')
password_input.pack(ipady=6, pady=(1, 15))

# Create Account button
create_account_button = Button(root, text='Create Account', command=create_account)
create_account_button.pack(pady=(20, 10))

# Login button
login_button = Button(root, text='Login', command=handle_login)
login_button.pack(pady=(10, 20))

root.mainloop()
