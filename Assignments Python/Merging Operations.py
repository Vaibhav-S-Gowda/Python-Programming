import pandas as pd

# Load CSV files
customer = pd.read_csv("customer.csv")
orders = pd.read_csv("orders.csv")
payment = pd.read_csv("payment.csv")
products = pd.read_csv("products.csv")

# -----------------------------------------------------------------------------------
''' Combine orders and customers data to show order_id customer_name city and region. 
    Use an appropriate merge type. '''

# Merge orders with customers
orders_customers = orders.merge(customer, on="customer_id", how="left")

# Select required fields
combined_oc = orders_customers[["order_id", "customer_name", "city", "region"]]

print("\nOrders with customer details:")
print(combined_oc)

# -----------------------------------------------------------------------------------
''' Merge orders with products to calculate order value for each order line.
    Order value is quantity multiplied by unit_price. '''

orders_products = orders.merge(products, on ="product_id", how="left")
orders_products["Order_Value"] = orders_products["quantity"] * orders_products["unit_price"]
print("\nOrders with order value:")
print(orders_products[["order_id", "product_id", "quantity", "Order_Value"]])

