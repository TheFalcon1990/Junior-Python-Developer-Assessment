import random
from faker import Faker
from pathlib import Path
import pandas as pd
import json

class DataGenerator:
    """Generates synthetic customer and order data using Faker."""

    def __init__(self, database, config: dict):
        """Initializes the Faker generator and loads the config."""
        self.fake = Faker()
        self.db = database
        self.config = config
        self.row_count = self.config['row_count']

    def generate_bulk_values(self, table_name: str, data: list):
        """Generates bulk SQL values for insertion."""
        keys = data[0].keys()
        placeholders = ", ".join(["?" for _ in keys])
        values = [tuple(item.values()) for item in data]
        return placeholders, values

    def generate_data(self, table_name: str) -> list:
        """Generates data for a given table based on the config."""
        columns = [col for col in self.config['database'][table_name].keys() if 'FOREIGN KEY' not in col]
        data = []

        for i in range(1, self.row_count + 1):
            row = {}
            for col in columns:
                if col == 'customer_id' or col == 'order_id':
                    row[col] = i
                elif col == 'first_name':
                    row[col] = self.fake.first_name()
                elif col == 'surname':
                    row[col] = self.fake.last_name()
                elif col == 'email':
                    row[col] = self.fake.email()
                elif col == 'status':
                    row[col] = random.choice(["active", "archived", "suspended"])
                elif col == 'product_name':
                    row[col] = f"{self.fake.word().capitalize()} {self.fake.word().capitalize()}"
                elif col == 'quantity':
                    row[col] = random.randint(1, 10)
                elif col == 'price':
                    row[col] = round(random.uniform(10.0, 100.0), 2)
            data.append(row)

        return data

    def generate_and_insert(self):
        """Generates and inserts data into the database."""
        customers = self.generate_data("CUSTOMERS")
        orders = self.generate_data("ORDERS")

        self.db.insert_data("CUSTOMERS", customers)
        self.db.insert_data("ORDERS", orders)