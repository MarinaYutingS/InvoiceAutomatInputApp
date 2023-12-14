import tkinter as tk
from tkinter import ttk
import pandas as pd

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management App")

        self.product_data = pd.DataFrame(columns=['Item ID', 'Product Name', 'Quantity', 'Price', 'Cost', 'Stock'])

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for Item ID
        self.label_item_id = ttk.Label(self.root, text="Item ID:")
        self.label_item_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_item_id = ttk.Entry(self.root)
        self.entry_item_id.grid(row=0, column=1, padx=10, pady=10)

        # Button to fetch product details
        self.fetch_button = ttk.Button(self.root, text="Fetch Product", command=self.fetch_product)
        self.fetch_button.grid(row=0, column=2, padx=10, pady=10)

        # Labels and Entries for Product Name, Quantity, and Price
        self.label_product_name = ttk.Label(self.root, text="Product Name:")
        self.label_product_name.grid(row=1, column=0, padx=10, pady=10)
        self.entry_product_name = ttk.Entry(self.root, state=tk.DISABLED)
        self.entry_product_name.grid(row=1, column=1, padx=10, pady=10)

        self.label_quantity = ttk.Label(self.root, text="Quantity:")
        self.label_quantity.grid(row=2, column=0, padx=10, pady=10)
        self.entry_quantity = ttk.Entry(self.root)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=10)

        self.label_price = ttk.Label(self.root, text="Price:")
        self.label_price.grid(row=3, column=0, padx=10, pady=10)
        self.entry_price = ttk.Entry(self.root)
        self.entry_price.grid(row=3, column=1, padx=10, pady=10)

        # Button to calculate and generate CSV
        self.calculate_button = ttk.Button(self.root, text="Calculate and Generate CSV", command=self.calculate_and_generate_csv)
        self.calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def fetch_product(self):
        item_id = self.entry_item_id.get()

        # Assume this function fetches product details based on the item_id
        # Replace this with your actual data retrieval logic
        product_name, is_new = self.get_product_details(item_id)

        self.entry_product_name.config(state=tk.NORMAL)
        self.entry_product_name.delete(0, tk.END)
        self.entry_product_name.insert(0, product_name)
        self.entry_product_name.config(state=tk.DISABLED)

        if is_new:
            self.baptize_product()

    def get_product_details(self, item_id):
        # Replace this with your actual data retrieval logic
        # For simplicity, returning static data
        return f"Product-{item_id}", False

    def baptize_product(self):
        # Replace this with your actual baptism logic
        # For simplicity, using a messagebox
        tk.messagebox.showinfo("Baptize Product", "This product is new. Please baptize it.")

    def calculate_and_generate_csv(self):
        item_id = self.entry_item_id.get()
        product_name = self.entry_product_name.get()
        quantity = float(self.entry_quantity.get())
        price = float(self.entry_price.get())
        cost = quantity * price

        # Update product_data DataFrame
        self.product_data = self.product_data.append({
            'Item ID': item_id,
            'Product Name': product_name,
            'Quantity': quantity,
            'Price': price,
            'Cost': cost,
            'Stock': 0  # Assuming stock is initially 0, update as needed
        }, ignore_index=True)

        # Generate CSV file
        self.product_data.to_csv(f"{item_id}_data.csv", index=False)

        tk.messagebox.showinfo("CSV Generated", "CSV file has been generated successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()
