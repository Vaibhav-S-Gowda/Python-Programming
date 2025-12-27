import pandas as pd

# Load CSV files
customer = pd.read_csv("customer.csv")
orders = pd.read_csv("orders.csv")
payment = pd.read_csv("payment.csv")
products = pd.read_csv("products.csv")

# --------------------------------------------------------
''' Find the total quantity ordered for each product_id. 
    Sort the result in descending order of quantity.'''

# Group by product_id and sum the quantities
total_quantity_per_product = orders.groupby("product_id")["quantity"].sum().reset_index()

# Sort in descending order of quantity
total_quantity_per_product = total_quantity_per_product.sort_values(by="quantity", ascending=False)

# Display the result
print("\nTotal quantity ordered per product (descending):")
print(total_quantity_per_product)

# -------------------------------------------------------------------------------------------
''' Calculate the number of orders placed in each region. Display region and order count. '''

orders_per_region = orders.groupby("region")["order_id"].count().reset_index()

# Rename orders for clarity
orders_per_region.columns = ['region', "order_count"]

# Display results
print("\nNumber of orders per region:")
print(orders_per_region)

# -------------------------------------------------------------------------------------------
''' Compute the average unit price of products grouped by category '''

# Compute average unit price grouped by category
avg_price_per_category = products.groupby("category")["unit_price"].mean().reset_index()

# Rename columns for clarity
avg_price_per_category.columns = ["category", "average_unit_price"]

# Display results
print("\nAverage unit price per product category:")
print(avg_price_per_category)