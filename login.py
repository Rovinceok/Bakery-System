from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
import time

root=Tk()
root.geometry("1400x1200")
root.title("BARATON BAKERY ORDER SYSTEM")


img = Image.open("Images/photo.jpg")
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_image = ImageTk.PhotoImage(img)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def validate_username(username):
    if not username.isalpha():
        messagebox.showerror( "Error", "Username cannot contain numbers")

        return False
    return True

validate_command = root.register(validate_username)

def cart():
    root.destroy()
    import cart
    
def admin_login():
    time.sleep(0.1)
    root.destroy()
    import adminlogin

def register():
    root.destroy()
    import register


def homepage():
    root.destroy()
    import homepage


def show_p():
    if show_password.get():
        pass_entry.config(show="")
    else:
        pass_entry.config(show="*")


def user_login():
    username = user_entry.get()
    u_password = pass_entry.get()
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="dbms2022", database="class_project")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=%s AND u_password=%s"
        cursor.execute(query, (username, u_password))
        row = cursor.fetchone()
        if username == "" or u_password == "":
          messagebox.showerror("Error", "Please fill out all the fields. Username or password cannot be empty")
        elif row is not None:
            cart()
       
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


user_label = Label(root, text="BARATON BAKERY ORDER SYSTEM",background="#C49A42", font=("Elephant", 28),width=100,fg="#7E2A11")
user_label.pack(pady=5)


user_label = Label(root, text="TASTE IT!...FEEL IT!...", font=("Bradley Hand ITC", 25), fg="blue",background="#A2BED5")
user_label.place(x=520,y=597)


user_labex = Frame(root,width=400,height=300,background="#C49A42",padx=5)
user_labex.place(x=3,y=70 )

user_label = Label(root, text="LOGIN TO YOUR ACCOUNT", font=("Arial bold", 17),fg="#7E2A11",background="#C49A42")
user_label.place(x=12,y=75 )
user_label = Label(root, text="Username:",font=("Arial bold",12),background="#C49A42" )
user_label.place(x=12,y=125)
user_entry = Entry(root,width=30 , font=('Arial', 10, 'bold'),validate="key", validatecommand=(validate_command, '%S'))
user_entry.place(x=120,y=125)

# Password
pass_label = Label(root, text="Password:",font=("Arial bold",12) ,background="#C49A42")
pass_label.place(x=12,y=165)
pass_entry = Entry(root, show="*",width=30 , font=('Arial', 10, 'bold'))
show_password_checkbox = Checkbutton(root, text="Show password", variable=show_password, command=show_p,width=12,height=1,foreground="blue",font=("Arial bold",12),background="#C49A42")
pass_entry.place(x=120,y=165)
show_password_checkbox.place(x=12,y=215)


b2=Button(width=15,text='Forgot password?',border=0,bg='white',fg='blue',height=1,font=("Arial bold",10) ,background="#C49A42")
b2.place(x=200,y=215)

# Login button
login_button = Button(root, text="Sign in",font=("Arial bold",11), width=20,height=1, command=user_login ,bg="#C49A42")
login_button.place(x=138,y=265)
login_button = Button(root, text="Create account",font=("Arial bold",11), width=20,height=1, command=register ,bg="#C49A42")
login_button.place(x=138,y=315)

login_button = Button(root, text="Admin",font=("elephant",14), width=5,height=1, command=admin_login ,bg="#C49A42")
login_button.place(x=1260,y=65)

root.mainloop()

