# ------------------------------------
#      Data Loading and Inspection
# ------------------------------------

# Given four CSV files representing customers products orders and payments. Load all files into Pandas DataFrames. Display the number of rows and columns for each DataFrame.

import pandas as pd

# Load CSV files
customers = pd.read_csv("customer.csv")
orders = pd.read_csv("orders.csv")
payment = pd.read_csv("payment.csv")
products = pd.read_csv("products.csv")

# Display number of rows and columns for each DataFrame
print("Customer Dataframe: ", customers.shape)
print("Orders Dataframe: ", orders.shape)
print("Payment Dataframe: ", payment.shape)
print("Products Dataframe: ", products.shape)