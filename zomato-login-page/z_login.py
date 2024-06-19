from tkinter import *
from tkinter import messagebox,font
import pandas as pd
import os

# Function to save account data
def create_account():
    email = signup_email_input.get()
    password = signup_password_input.get()

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
            signup_email_input.delete(0, END)
            signup_password_input.delete(0, END)
    else:
        messagebox.showerror('Error', 'Please fill in both fields')

# Function to handle login
def handle_login():
    email = login_email_input.get()
    password = login_password_input.get()

    if os.path.exists('users.csv'):
        df = pd.read_csv('users.csv')
        if ((df['Email'] == email) & (df['Password'] == password)).any():
            messagebox.showinfo('Login Status', 'Login successful')
        else:
            messagebox.showerror('Login Status', 'Invalid email or password')
    else:
        messagebox.showerror('Login Status', 'No accounts found. Please create an account first.')

# Function to show the sign up form
def show_signup():
    login_frame.pack_forget()
    signup_frame.pack()

# Function to show the login form
def show_login():
    signup_frame.pack_forget()
    login_frame.pack()

# Root window
root = Tk()
root.title('Zomato Login Form')
root.geometry('650x650')
root.configure(bg='red')

# Load the Zomato branding image
zomato_logo = PhotoImage(file='zomato-login-page\zomato.png')

# Branding image label
icon_label = Label(root, image=zomato_logo , bg='red')
icon_label.pack(pady=(20, 5))


custom_font = font.Font(family='Arial', size=14)
# Welcome label
welcome_label = Label(root, text='Welcome to Zomato', fg='white', bg='red',font = custom_font)
welcome_label.pack(pady=(5, 5))

# Login and Sign Up buttons
login_button = Button(root, text='Sign In', command=show_login, bg='white', fg='red',font = custom_font)
login_button.pack(pady=(10, 10))

signup_button = Button(root, text='Sign Up', command=show_signup, bg='white', fg='red' , font = custom_font)
signup_button.pack(pady=(10, 10))

# Sign Up Frame
signup_frame = Frame(root, bg='red')
signup_email_label = Label(signup_frame, text='Enter Email', fg='white', bg='red',font = custom_font)
signup_email_label.pack(pady=(20, 5))


signup_email_input = Entry(signup_frame, width=50)
signup_email_input.pack(ipady=6, pady=(1, 15))

signup_password_label = Label(signup_frame, text='Enter Password:', fg='white', bg='red',font = custom_font)
signup_password_label.pack(pady=(20, 5))


signup_password_input = Entry(signup_frame, width=50, show='*')
signup_password_input.pack(ipady=6, pady=(1, 15))

create_account_button = Button(signup_frame, text='Create Account:', command=create_account, bg='white', fg='red',font = custom_font)
create_account_button.pack(pady=(20, 10))

# Login Frame
login_frame = Frame(root, bg='red')
login_email_label = Label(login_frame, text='Enter Email:', fg='white', bg='red',font = custom_font)
login_email_label.pack(pady=(20, 5))

login_email_input = Entry(login_frame, width=50)
login_email_input.pack(ipady=6, pady=(1, 15))

login_password_label = Label(login_frame, text='Enter Password:', fg='white', bg='red',font = custom_font)
login_password_label.pack(pady=(20, 5))


login_password_input = Entry(login_frame, width=50, show='*')
login_password_input.pack(ipady=6, pady=(1, 15))

login_button_frame = Button(login_frame, text='Login', command=handle_login, bg='white', fg='red',font = custom_font)
login_button_frame.pack(pady=(20, 10))

root.mainloop()
