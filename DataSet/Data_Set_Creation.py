from faker import Faker
import pandas as pd
import random
import sqlite3
import os

fake = Faker()

# Database setup
db_name = "assessment.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Drop existing tables if they exist (for repeatability)
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS customers")

# Create customers table with PRIMARY KEY
cursor.execute("""
    CREATE TABLE Customers (
        Customer_id INTEGER PRIMARY KEY,
        First_name TEXT NOT NULL,
        Surname TEXT NOT NULL,
        Email TEXT NOT NULL,
        Status TEXT NOT NULL
    )
""")

# Create orders table with FOREIGN KEY
cursor.execute("""
    CREATE TABLE Orders (
        Order_id INTEGER PRIMARY KEY,
        Customer_id INTEGER NOT NULL,
        Product_name TEXT NOT NULL,
        Quantity INTEGER NOT NULL,
        Unit_price REAL NOT NULL,
        FOREIGN KEY (Customer_id) REFERENCES Customers(Customer_id)
    )
""")

# Generate Customers data
customers = []
for i in range(1, 51):
    customer = {
        "Customer_id": i,
        "First_name": fake.first_name(),
        "Surname": fake.last_name(),
        "Email": fake.email(),
        "Status": random.choice(["active", "archived", "suspended"])
    }
    customers.append(customer)
    cursor.execute("""
        INSERT INTO customers (Customer_id, First_name, Surname, Email, Status)
        VALUES (?, ?, ?, ?, ?)
    """, (customer["Customer_id"], customer["First_name"], customer["Surname"], 
          customer["Email"], customer["Status"]))

# Generate Orders data
orders = []
for i in range(1, 51):
    order = {
        "Order_id": i,
        "Customer_id": random.randint(1, 50),  # Link to existing customers (1-50)
        "Product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "Quantity": random.randint(1, 10),
        "Unit_price": round(random.uniform(10.0, 100.0), 2)
    }
    orders.append(order)
    cursor.execute("""
        INSERT INTO orders (Order_id, Customer_id, Product_name, Quantity, Unit_price)
        VALUES (?, ?, ?, ?, ?)
    """, (order["Order_id"], order["Customer_id"], order["Product_name"], 
          order["Quantity"], order["Unit_price"]))

# Commit changes and close connection
conn.commit()
conn.close()

# Also export to CSV for reference
df_customers = pd.DataFrame(customers)
df_customers.to_csv("customers.csv", index=False)

df_orders = pd.DataFrame(orders)
df_orders.to_csv("orders.csv", index=False)

print(f"✓ Database '{db_name}' created successfully")
print(f"✓ Customers table created with {len(customers)} records")
print(f"✓ Orders table created with {len(orders)} records")
print(f"✓ CSV files exported: customers.csv and orders.csv")