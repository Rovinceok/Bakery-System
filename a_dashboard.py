from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

def orders():
    root.destroy()
    import orders


def reg_customer():
    root.destroy()
    import register

def customers():
    root.destroy()
    import customers

root=Tk()
root.configure(background="gray")
root.geometry("1400x1200")



user_label = Label(root, text="ADMIN", font=("elephant", 33),background="gray" )
user_label.pack(pady=5)

login_button = Button(root, text="Customers",font=("elephant", 13), width=8,height=1, command=customers ,bg="light blue",relief="groove")
login_button.place(x=38,y=65)

login_button = Button(root, text="orders",font=("elephant", 13), width=5,height=1, bg="light blue",relief="groove",command=orders)
login_button.place(x=338,y=65)

login_button = Button(root, text="Add customer",font=("elephant", 13), width=10,height=1, bg="light blue",command=reg_customer,relief="groove")
login_button.place(x=898,y=65)





root.mainloop()

