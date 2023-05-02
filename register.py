import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
import hashlib

import os
from datetime import date
from datetime import datetime
from tkinter import messagebox
import mysql.connector

root = Tk()
root.configure(background="gray")
root.geometry("1400x1200")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dbms2022",
  database="class_project"
)

mycursor = mydb.cursor()

def hash_password():
    password = password_entry.get()
    # encode the password string to bytes
    password_bytes = password.encode('utf-8')
    # use SHA-256 hash function to hash the password
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    # clear the password entry field
    password_entry.delete(0, END)

def insert_data():
    username = username_entry.get()
    email = email_entry.get()
    phone_no = phone_entry.get()
    location = location_var.get()
    u_password = password_entry.get()
    # password_bytes = u_password.encode('utf-8')
    # hashed_password = hashlib.sha256(password_bytes).hexdigest()
    

    mycursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = mycursor.fetchone()      
    if result:
        messagebox.showerror( "Error","Username already exists. Enter a different username!")


    elif username == "" or email == "" or phone_no == "" or location == "" or  u_password == "":
      messagebox.showerror( "Empty Form","All fields are required! Try again!")
    else:
     sql = "INSERT INTO users (username, email, phone_no,location,u_password) VALUES (%s, %s, %s,%s,%s)"
     val = (username, email, phone_no, location,  u_password)
     messagebox.showinfo( "Success", "Registration successful. Thank you for registering.")
     login()

    mycursor.execute(sql, val)
    mydb.commit()
        


   
    
     
show_password = BooleanVar()

def show_p():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def login():
   root.destroy()
   import login


def validate_phone(phone):
    if not phone.isdigit():
        messagebox.showerror( "Error", "Phone number cannot contain letters!.")

        return False
    return True

validate_cmds = root.register(validate_phone)


def validate_username(username):
    if not username.isalpha():
        messagebox.showerror( "Error", "Username cannot contain numbers!.")

        return False
    return True

validate_cmd = root.register(validate_username)



user_labex = Frame(root,width=400,height=330,background="#808080",padx=5)
user_labex.place(x=3,y=0 )



user_label = Label(root, text="ALREADY HAVE AN ACCOUNT?", font=("Arial bold", 13),background="#808080")
user_label.place(x=577,y=58 )

submit_button = tk.Button(root, text="LOGIN",font=("Arial bold",12) ,width=15, bg="pink", command=login ,background="#808080")
submit_button.place(x=630,y=120)

user_label = Label(root, text="CREATE YOUR ACCOUNT", font=("Arial bold", 12),background="#808080")
user_label.place(x=17,y=5 )
username_label = tk.Label(root, text="Username", width=14 ,font=("Arial bold",12),background="#808080")
username_label.place(x=17,y=36)
username_entry = Entry(root,width=30,validate="key", validatecommand=(validate_cmd, '%S'))
username_entry.place(x=197,y=36)

email_label = tk.Label(root, text="Email" , width=14 ,font=("Arial bold",12),background="#808080")
email_label.place(x=17,y=66)
email_entry = Entry(root,width=30)
email_entry.place(x=197,y=66)

phone_label = tk.Label(root, text="Phone Number" , width=14 ,font=("Arial bold",12),background="#808080")
phone_label.place(x=17,y=96)
phone_entry = Entry(root,width=30 ,validate="key", validatecommand=(validate_cmds, '%S'))
phone_entry.place(x=197,y=96)

location_label = tk.Label(root, text="Location" , width=14 ,font=("Arial bold",12),background="#808080")
location_label.place(x=17,y=126)
# location_entry = Entry(root,width=30 )
# location_entry.place(x=197,y=126)

location_var = tk.StringVar()
location_menu = ttk.Combobox(root, textvariable=location_var, values=["Baraton Center", "Chemundu","Lavingtone","Richmond",
                                                                      "Urban estate","Runda","Poa place","Chesumei"],width=27)
location_menu.place(x=197,y=126)

password_label = tk.Label(root, text="Password" , width=14,font=("Arial bold",12),background="#808080")
password_label.place(x=17,y=156)
password_entry = Entry(root, show="*",width=30)
password_entry.place(x=197,y=156)
show_password_checkbox = Checkbutton(root, text="Show password", variable=show_password, command=show_p,width=14,height=1, foreground="blue",font=("Arial bold",12),background="#808080")
show_password_checkbox.place(x=197,y=200)


    # Create a button to submit the registration form
submit_button = tk.Button(root, text="Submit",font=("Arial bold",15) ,width=10,bg="#808080", command=insert_data )
submit_button.place(x=102,y=256)

root.mainloop()





