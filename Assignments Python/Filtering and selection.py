import pandas as pd

# Load CSV files
customer = pd.read_csv("customer.csv")
orders = pd.read_csv("orders.csv")
payment = pd.read_csv("payment.csv")
products = pd.read_csv("products.csv")

# ************************************************************************
''' Analyze only South region orders. 
    Filter the orders DataFrame to show records from the South region. '''

south_orders = orders[orders["region"] == "South"]
print("\nSouth Region Orders: ")
print(south_orders)

# Verify Count
print("\nNumber of South region orders: ", len(south_orders))