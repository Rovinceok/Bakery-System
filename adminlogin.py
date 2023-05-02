from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk


root=Tk()
root.configure(background="gray")
root.geometry("1400x1200")
def user():
    root.destroy()
    import login

def admin():
    root.destroy()
    import a_dashboard


def show_p():
    if show_password.get():
        pass_entry.config(show="")
    else:
        pass_entry.config(show="*")


def a_login():
    username = user_entry.get()
    a_password = pass_entry.get()
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="dbms2022", database="class_project")
        cursor = connection.cursor()
        query = "SELECT * FROM admin WHERE username=%s AND password=%s"
        cursor.execute(query, (username, a_password))
        row = cursor.fetchone()
        if row is not None:
            admin()
        if username == "" or a_password == "":
         messagebox.showerror("Error", "All fields are required. Try again!")
        else:
            messagebox.showerror("Login", "Invalid username or password")
    except mysql.connector.Error as error:
        print("Failed to login to database: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

show_password = BooleanVar()




user_labex = Frame(root,width=400,height=300,background="#808080",padx=5)
user_labex.place(x=3,y=70 )


user_label = Label(root, text="ADMIN LOGIN", font=("elephant", 26),background="#808080")
user_label.pack(pady=5)

user_label = Label(root, text="ENTER LOGIN DETAILS", font=("elephant", 14),background="#808080")
user_label.place(x=12,y=75 )
user_label = Label(root, text="Username:",font=("elephant",13) ,background="#808080")
user_label.place(x=12,y=125)
user_entry = Entry(root,width=30 , font=('Arial', 10, 'bold'))
user_entry.place(x=120,y=125)

# Password
pass_label = Label(root, text="Password:",font=("elephant",13) ,background="#808080")
pass_label.place(x=12,y=165)
pass_entry = Entry(root, show="*",width=30 , font=('Arial', 10, 'bold'))
show_password_checkbox = Checkbutton(root, text="Show password", variable=show_password, command=show_p,width=12,foreground="blue",font=("Arial bold",12),background="#808080")
pass_entry.place(x=120,y=165)
show_password_checkbox.place(x=12,y=215)

# Login button
login_button = Button(root, text="LOGIN", font=('Arial', 10, 'bold'), width=15,height=2, command=a_login ,bg="gray")
login_button.place(x=138,y=265)

login_button = Button(root, text="HOME", font=('Arial', 10, 'bold'), width=11,height=2, command=user ,bg="#808080")
login_button.place(x=738,y=165)


root.mainloop()

