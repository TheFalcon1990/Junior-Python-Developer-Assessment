from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []
for i in range(1, 51):
    customers.append({
        "customer_id": i,
        "first_name": fake.first_name(),
        "surname": fake.last_name(),
        "email": fake.email(),
        "status": random.choice(["active", "archived", "suspended"])
    })

df = pd.DataFrame(customers)
df.to_csv("customers.csv", index=False)

# Generate Orders data
orders = []
for i in range(1, 51):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 30),  # Link to existing customers
        "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),  # Fake product name
        "quantity": random.randint(1, 10),
        "unit_price": round(random.uniform(10.0, 100.0), 2)
    })

df_orders = pd.DataFrame(orders)
df_orders.to_csv("orders.csv", index=False)