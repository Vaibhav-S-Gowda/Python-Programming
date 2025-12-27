# ------------------------------------
#      Data Loading and Inspection
# ------------------------------------

import pandas as pd

# *****************************************************************************************
''' Given four CSV files representing customers products orders and payments.
    Load all files into Pandas DataFrames. 
    Display the number of rows and columns for each DataFrame. '''

# Load CSV files
customer = pd.read_csv("customer.csv")
orders = pd.read_csv("orders.csv")
payment = pd.read_csv("payment.csv")
products = pd.read_csv("products.csv")

# Display number of rows and columns for each DataFrame
print("Customer Dataframe: ", customer.shape)
print("Orders Dataframe: ", orders.shape)
print("Payment Dataframe: ", payment.shape)
print("Products Dataframe: ", products.shape)

# *****************************************************************************************
''' Column names contain mixed casing and spacing risks. Inspect column names for consistency.
    List all column names for each DataFrame '''

print("\n--- Column Names Inspection ---")
print("Customer Columns: ", list(customer.columns))
print("Orders Columns: ", list(orders.columns))
print("Payment Columns: ", list(payment.columns))
print("Products Columns: ", list(products.columns))

# Optional: Check for mixed casing / spaces / risky names
def risky_names(df):
    return [col for col in df.columns if (" " in col) or (col != col.lower())]

print("\nPossible risky column names (contain spaces or inconsistent casting): ")
print("Customers: ", risky_names(customer))
print("Order: ", risky_names(orders))
print("Payments: ", risky_names(payment))
print("Products: ", risky_names(products))

# *****************************************************************************************
''' Order dates are stored as strings. 
    Convert the order_date column into datetime format. Verify the datatype change '''

# Convert order_date column to datetime
orders["order_date"] = pd.to_datetime(orders["order_date"])

# Verify the datatype change
print("\nData types after converting order_date: ")
print(orders.dtypes)