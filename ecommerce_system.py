import pyodbc
from data_base_connection import database_connection
from product import Product
from prettytable import PrettyTable

class Ecommerce:
    def __init__(self):
        self.store_products = []
        
    def add_product_in_store(self, name, quantity_in_stock, price):
        
        # Connect to MSSQL database
        conn = database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO products (name, quantity_in_stock, price) VALUES (?, ?, ?)",(name.title(), quantity_in_stock, price))
            # Commit the changes and close the connection
            print(f'Product {name} added successfully.')
            conn.commit()
            conn.close()
        except:
            ValueError('Check Values.')
            
    def update_product_in_store(self, product_name, new_quantity, new_price):
        
        # Connect to MSSQL database
        conn = database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE products SET quantity_in_stock = ?, price = ? WHERE name = ?", (new_quantity, new_price, product_name))
            # Commit the changes and close the connection
            print(f'Product {product_name} updated successfully.')
            conn.commit()
            conn.close()
        except:
            ValueError('Check Values.')
        
        
    
    def get_data(self):
        
        # Connect to MSSQL database
        conn = database_connection()
        cursor = conn.cursor()
        # Retrieve products from the database
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        # Create Product objects from database rows
        for row in rows:
            product = Product(row[0], row[1], row[2], row[3])
            self.store_products.append(product)
        conn.commit()
        conn.close()
        
    def disp_product_info(self):
        
        products = PrettyTable(["Product ID.", "Product Name", "Available Quantity", "Product Price"])
        
        print('==================================================================')
        print('=====================WELCOME TO XYZ COMPANY=======================')
        print('==================================================================')        
        
        for product in self.store_products:
            products.add_row([product.product_id, product.name, product.quantity_in_stock, product.price])
        
        print(products)

