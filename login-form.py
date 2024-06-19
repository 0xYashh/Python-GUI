from tkinter import *
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == '0xyash@gmail.com' and password == 'yash#777':
        messagebox.showinfo('Login Status', 'Yayyy! Login successful')
    else:
        messagebox.showerror('Login Status', 'Login failed')

root = Tk()
root.title('Login Form')
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

# Submit button
submit_button = Button(root, text='Submit', command=handle_login)
submit_button.pack(pady=(20, 20))

root.mainloop()
