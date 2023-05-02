from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

# Connect to the XAMPP database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dbms2022",
    database="class_project"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SELECT statement
mycursor.execute("SELECT * FROM users order by Registration_date desc  ")

# Get the results
results = mycursor.fetchall()

# Create the Tkinter window
root=Tk()
root.configure(background="gray")
root.geometry("1400x1200")

user_label = Label(root, text="CUSTOMERS LIST", font=("Elephant", 17),background="#808080")
user_label.pack(pady=5)
style = ttk.Style()
style.configure("Treeview.Heading", foreground="Blue", background="yellow" , font=("Arial bold", 12))
style.configure("table.insert.values", foreground="Blue", background="yellow" , font=("Arial bold", 12))

def back():
    root.destroy()
    import a_dashboard

    
login_button = Button(root, text="Back",font=("elephant", 12), width=5, bg="#808080",command=back)
login_button.place(x=18,y=15)

# Create the table
table = ttk.Treeview(root, columns=("username", "email", "phone_no", "location", "u_password", "Registration_date"), show="headings",height=10)
table.heading("username", text="NAME")
table.heading("email", text="EMAIL")
table.heading("phone_no", text="PHONE NUMBER" )
table.heading("location", text="LOCATION")
table.heading("u_password", text="PASSWORD")
table.heading("Registration_date", text="REGISTRATION DATE")

# Add the records to the table
for record in results:
    table.insert("", "end", values=(record[0], record[1], record[2], record[3], record[4], record[5]))
# Pack the table and start the main loop
table.place(x=17,y=70)
table.winfo_geometry()
# Start the Tkinter event loop
root.mainloop()
