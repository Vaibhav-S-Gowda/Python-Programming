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

# ************************************************************************
''' Management wants to see only Corporate customers.
    Filter the customers DataFrame to show Corporate segment customers'''

corporate_customers = customer[customer["segment"] == "Corporate"]
print("\nCorporate Custumer: ")
print(corporate_customers)

# Verify Count
print("\nNumber of Corporate customers:", len(corporate_customers))

# ************************************************************************
''' Identify all orders where quantity is greater than 10.
    Display order_id customer_id and quantity'''

high_quantity_orders = orders[orders["quantity"] > 10][["order_id", "customer_id", "quantity"]]
print("\nOrders with quantity greater than 10: ")
print(high_quantity_orders)