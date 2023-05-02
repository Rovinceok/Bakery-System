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
mycursor.execute("SELECT * FROM orders order by order_date desc")

# Get the results
results = mycursor.fetchall()

# Create the Tkinter window
root=Tk()
root.configure(background="gray")
root.geometry("1400x1200")

user_label = Label(root, text="ORDER HISTORY", font=("Arial bold", 13),background="#25E86F")
user_label.pack(pady=5)
style = ttk.Style()
style.configure("Treeview.Heading", foreground="Blue", background="yellow" , font=("Arial bold", 12))
style.configure("table.insert.values", foreground="Blue", background="yellow" , font=("Arial bold", 12))

def back():
    root.destroy()
    import a_dashboard

    
login_button = Button(root, text="<< Back",font=("Arial bold", 10), width=7, bg="#25E86F",command=back)
login_button.place(x=18,y=15)

# Create the table
table = ttk.Treeview(root, columns=("name", "phone", "location", "item", "quantity", "total","order_date"), show="headings",height=10)
table.heading("name", text="NAME")
table.heading("phone", text="PHONE NUMBER")
table.heading("location", text="LOCATION" )
table.heading("item", text="ITEM")
table.heading("quantity", text="QUANTITY")
table.heading("total", text="TOTAL ORDER (ksh)")
table.heading("order_date", text="DATE ORDERED")

# Add the records to the table
for record in results:
    table.insert("", "end", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
# Pack the table and start the main loop
table.place(x=1,y=70)
table.winfo_geometry()
# Start the Tkinter event loop
root.mainloop()
