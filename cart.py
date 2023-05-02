import tkinter as tk
import sqlite3
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime






# Connect to the database


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dbms2022",
  database="class_project"
)

mycursor = mydb.cursor()
conn = sqlite3.connect('orders.db')
c = conn.cursor()

# Create orders table if not exists


# Item prices
item_prices = {'Crate': 1200, 'Bara 800g': 120, 'Bara 400g': 80, 'Bara 40g': 35, 'Scones': 60}



def validate_username(username):
    username=name_var.get()
    if not username.isalpha():
        print("Error: Username should only contain letters")
        return False
    return True
# validate_command = tk.root.register(validate_username)

def validate_phone(phone):
    if not phone.isdigit():
        messagebox.showerror( "Error", "Phone number cannot contain letters!.")

        return False
    return True

# validate_cmds = root.register(validate_phone)

def log_out():
    root.destroy()
    import login
# Function to add item to cart
def add_to_cart():
    # Get selected item and quantity
    item = item_var.get()
    quantity = quantity_var.get()
    
    # Calculate total order amount
    total = item_prices[item] * quantity
        
    if name_var.get() == "" or phone_var.get() == "" or location_var.get() == "" or item == "" or quantity == "" or total == "":
      messagebox.showerror( "Empty Form","All fields are required! Try again!")    
    # Insert order into database
    else:
     sql = "INSERT INTO orders (name, phone, location,item,quantity,total) VALUES (%s, %s, %s,%s,%s,%s)"
     val = (name_var.get(),phone_var.get(), location_var.get(), item, quantity, total)

     messagebox.showinfo("Confirm","Your total order amount is Ksh:" + str(total))

     messagebox.showinfo( "Success", "Order sent successfully. Thank you for choosing Baraton Bakery!")

    confirm_label.config(text=f'{quantity} {item} (s) added to cart.\n Your total order is Ksh. { str(total)}', font=("Arial bold", 16),background="#F0F0F0",fg="black")
    confirm_label.place(x=1000,y=370)

    
    

    mycursor.execute(sql, val)
    mydb.commit()

    

    
    # Clear selection
    item_var.set('')
    quantity_var.set(1)
    

# Create GUI
root = tk.Tk()
root.geometry("1400x1400")
root.configure(background="#F0F0F0")
root.title('Bakery Order Cart')

def update_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")
    time_label.config(text=current_time)
    time_label.after(1000, update_time) # Update every second

# Create the main Tkinter window and label
time_label = tk.Label(root, font=("Helvetica", 13), bg="#F0F0F0", fg="blue")
time_label.place(x=1130,y=450)

# Call the update_time function to start the clock
update_time()



user_label = tk.Label(root, text="WELCOME TO OUR PRODUCT CATALOG, CHOOSE WHAT TO ORDER", font=("Elephant", 19),fg="#B96A2B")
user_label.place(x=150,y=5 )



user_labex = tk.Frame(root,width=490,height=300,background="#FFFFFF",padx=35,pady=43)
user_labex.place(x=490,y=370 )
# Create widgets


img = Image.open("Images/2.jpg")
img=img.resize((210, 210))

photo1 = ImageTk.PhotoImage(img)
label = tk.Label(image=photo1)
label.place(x=12,y=62)

user_label = tk.Label(root, text="Bara 800g", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=17,y=298 )
user_label = tk.Label(root, text="Ksh. 120.00", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=17,y=330 )


img1 = Image.open("Images/menu/400g.jpg")
img1=img1.resize((210, 210))

photo = ImageTk.PhotoImage(img1)

label = tk.Label(image=photo)
label.place(x=280,y=62)

user_label = tk.Label(root, text="Bara 400g", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=357,y=298 )
user_label = tk.Label(root, text="Ksh. 80.00", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=357,y=330 )



img2 = Image.open("Images/menu/40g.jpg")
img2=img2.resize((210, 210))
photo3 = ImageTk.PhotoImage(img2)
label = tk.Label(image=photo3)
label.place(x=555,y=62)

user_label = tk.Label(root, text="Bara 40g", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=637,y=298 )
user_label = tk.Label(root, text="Ksh. 35.00", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=637,y=330 )


img5 = Image.open("Images/menu/scones.jpg")
img5=img5.resize((210, 210))

photo4 = ImageTk.PhotoImage(img5)
label = tk.Label(image=photo4)
label.place(x=820,y=62)

user_label = tk.Label(root, text="Scones", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=910,y=298 )
user_label = tk.Label(root, text="Ksh. 60.00", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=910,y=330 )


img6 = Image.open("Images/menu/crate.jpg")
img6=img6.resize((210, 210))

photo7 = ImageTk.PhotoImage(img6)
label = tk.Label(image=photo7)
label.place(x=1090,y=62)

user_label = tk.Label(root, text="Crate (12 loaves)", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=1177,y=298 )
user_label = tk.Label(root, text="Ksh. 1200.00", font=("Arial bold", 11),background="#F0F0F0",fg="blue")
user_label.place(x=1177,y=330 )





user_label = tk.Label(root, text="Order made on:", font=("Arial bold", 12),background="#F0F0F0")
user_label.place(x=1000,y=450 )

user_label = tk.Label(root, text="FILL IN THE FORM BELOW TO COMPLETE YOUR ORDER", font=("Arial bold", 11),background="#FFFFFF")
user_label.place(x=517,y=390 )
# Create widgets
name_label = tk.Label(root, text='Full Name:', font=("Arial bold", 11),background="#FFFFFF")
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var, font=('Arial', 10, 'bold'))

name_label.place(x=589,y=436,width=90,height=26)
name_entry.place(x=690,y=436,width=180)

phone_label = tk.Label(root, text='Phone:', font=("Arial bold", 11),background="#FFFFFF")
phone_var = tk.StringVar()
phone_entry = tk.Entry(root, textvariable=phone_var, font=('Arial', 10, 'bold'))

phone_label.place(x=589,y=470,width=90,height=26)
phone_entry.place(x=690,y=470,width=180)




location_label = tk.Label(root, text='Location:', font=("Arial bold", 11),background="#FFFFFF")
location_var = tk.StringVar()
location_entry = tk.Entry(root, textvariable=location_var, font=('Arial', 10, 'bold'))


location_label.place(x=589,y=500,width=90,height=26)
location_entry.place(x=690,y=500,width=180)

item_label = tk.Label(root, text='Item:', font=("Arial bold", 11),background="#FFFFFF")
item_var = tk.StringVar()
item_dropdown = tk.OptionMenu(root, item_var, *item_prices.keys())

item_label.place(x=589,y=530,width=90,height=26)
item_dropdown.place(x=690,y=530,width=180)

quantity_label = tk.Label(root, text='Quantity:', font=("Arial bold", 11),background="#FFFFFF")
quantity_var = tk.IntVar(value=1)
quantity_spinbox = tk.Spinbox(root, from_=1, to=10, textvariable=quantity_var, font=('Arial', 10, 'bold'))


quantity_label.place(x=589,y=575,width=90,height=26)
quantity_spinbox.place(x=690,y=575,width=180)

add_button = tk.Button(root, text='Submit Order', command=add_to_cart, width=11,background="#1EE76A",font=("Elephant",14))


add_button.place(x=680,y=620)


logout = tk.Button(root, text='Log Out', width=9,background="#FFFFFF",font=("Arial bold",11),command=log_out)


logout.place(x=1200,y=10)

confirm_label = tk.Label(root, text='')


root.mainloop()