import tkinter as tk
from tkinter import messagebox



class BakeryOrderCart:
    def __init__(self, master):
        self.master = master
        master.title("Product Catalog")
        master.geometry("1200x800")

        # Create items and prices dictionary
        self.items = {
            "CRATE": 1400,
            "BARA120g": 120,
            "BARA60G": 65,
            "SCONS": 40,
            "Bagel": 150
        }

        # Create empty cart list
        self.cart = []

        # Create widgets
        self.item_label = tk.Label(master, text="Item",width=20,background="green", font=("Arial bold", 13))
        self.item_label.grid(row=0, column=0)

        self.price_label = tk.Label(master, text="Price (Ksh)",width=20,background="green", font=("Arial bold", 13))
        self.price_label.grid(row=0, column=1)

        self.quantity_label = tk.Label(master, text="Quantity",width=20,background="green", font=("Arial bold", 13))
        self.quantity_label.grid(row=0, column=2)

        self.add_to_cart_label = tk.Label(master, text="Add to Cart",width=20,background="green", font=("Arial bold", 13))
        self.add_to_cart_label.grid(row=0, column=3)

        self.cart_label = tk.Label(master, text="Cart",width=16,background="brown", font=("Arial bold", 13))
        self.cart_label.grid(row=0, column=4)

        # Add items to grid
        row_num = 1
        for item, price in self.items.items():
            item_label = tk.Label(master, text=item)
            item_label.grid(row=row_num, column=0)

            price_label = tk.Label(master, text=f"Ksh.{price:.2f}")
            price_label.grid(row=row_num, column=1)

            quantity_entry = tk.Entry(master, width=15)
            quantity_entry.grid(row=row_num, column=2)

            add_to_cart_button = tk.Button(master, text="Add to Cart",width=20,background="violet",height=1,pady=8,padx=5,
                                           command=lambda item=item, price=price, quantity_entry=quantity_entry: self.add_to_cart(item, price, quantity_entry))
            add_to_cart_button.grid(row=row_num, column=3)

            row_num += 1

        # Cart display
        self.cart_display = tk.Label(master, text="")
        self.cart_display.grid(row=1, column=4, rowspan=row_num)

        # Checkout button
        self.checkout_button = tk.Button(master, text="Checkout", command=self.checkout,background="pink",width=15,)
        self.checkout_button.grid(row=row_num+1, column=4)

    def add_to_cart(self, item, price, quantity_entry):
        quantity = quantity_entry.get()

        # Check if quantity is valid
        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            item_total = price * quantity

            # Add item to cart
            self.cart.append((item, price, quantity, item_total))

            # Update cart display
            self.cart_display.config(text=self.cart_display.cget("text") +
                                     f"{item} (Ksh{price:.2f}) x {quantity} = Ksh{item_total:.2f}\n")
        else:
            tk.messagebox.showerror("Invalid Quantity", "Please enter a valid quantity.")

    def checkout(self):
        # Calculate total
        total = sum(item[3] for item in self.cart)

        # Display total
        tk.messagebox.showinfo("Checkout", f"Your total is Ksh{total:.2f}.")

        # Clear cart
        self.cart = []
        self.cart_display.config(text="")
    

# Create window and start application
root = tk.Tk()
app = BakeryOrderCart(root)
root.mainloop()
