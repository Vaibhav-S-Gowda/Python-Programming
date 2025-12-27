import pandas as pd

# Load CSV files
customer = pd.read_csv("customer.csv")
orders = pd.read_csv("orders.csv")
payment = pd.read_csv("payment.csv")
products = pd.read_csv("products.csv")

# ------------------------------------------------------------------------------------
# 1. Combine orders and customers (order_id, customer_name, city, region)

orders_customers = orders.merge(customer, on="customer_id", how="left")
combined_oc = orders_customers[["order_id", "customer_name", "city", "region"]]

print("\nOrders with customer details:")
print(combined_oc)


# ------------------------------------------------------------------------------------
# 2. Merge orders + products to calculate order value

orders_products = orders.merge(products, on="product_id", how="left")
orders_products["Order_Value"] = orders_products["quantity"] * orders_products["unit_price"]

print("\nOrders with order value:")
print(orders_products[["order_id", "product_id", "quantity", "unit_price", "Order_Value"]])


# ------------------------------------------------------------------------------------
# 3. Merge all (orders + customers + products) and prepare final DataFrame

combined_all = orders.merge(customer, on="customer_id", how="left") \
                     .merge(products, on="product_id", how="left")

combined_all["Order_Value"] = combined_all["quantity"] * combined_all["unit_price"]

final_df = combined_all[[
    "order_id", "customer_name", "product_name", "category", "quantity", "Order_Value", "region"
]]

print("\nFinal combined DataFrame:")
print(final_df)


# ------------------------------------------------------------------------------------
# 4. Merge payments with full combined data (combined_all)

orders_payments = combined_all.merge(payment, on="order_id", how="left")

print("\nOrders merged with payment status:")
print(orders_payments[["order_id", "customer_name", "Order_Value", "payment_status"]])


# ------------------------------------------------------------------------------------
# 5. Identify Pending payments

pending_payments = orders_payments[orders_payments["payment_status"] == "Pending"]

print("\nOrders where payment is Pending:")
print(pending_payments[["order_id", "customer_name", "Order_Value", "payment_status"]])


# ------------------------------------------------------------------------------------
# 6. Calculate revenue only from Completed payments (group by region)

completed_payments = orders_payments[orders_payments["payment_status"] == "Completed"]

revenue_by_region = completed_payments.groupby("region")["Order_Value"].sum().reset_index()

print("\nTotal revenue from Completed payments grouped by region:")
print(revenue_by_region)

# -------------------------------------------------------------------------------
# 7. For each state, identify total number of orders and total revenue

orders_by_state = orders_payments.groupby("state").agg(
    total_orders = ("order_id", "count"),
    total_revenue = ("Order_Value", "sum")
).reset_index()

print("\nTotal Orders and Revenue by State:")
print(orders_by_state)
