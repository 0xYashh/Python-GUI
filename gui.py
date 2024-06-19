from tkinter import *

win=Tk()
win.geometry("750x250")
def click():
 mylabel.destroy()
 win.destroy()
mylabel=Label(win,text="hello")
mylabel.pack()
mybutton=Button(win,text="cancel",command=click)
mybutton.pack()
win.mainloop()
