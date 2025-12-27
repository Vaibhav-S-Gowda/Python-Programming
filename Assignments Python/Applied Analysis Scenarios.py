import pandas as pd

# Load CSV files
customer = pd.read_csv("customer.csv")
orders = pd.read_csv("orders.csv")
payment = pd.read_csv("payment.csv")
products = pd.read_csv("products.csv")

orders_customers = orders.merge(customer, on="customer_id", how="left")
combined_oc = orders_customers[["order_id", "customer_name", "city", "region"]]

orders_products = orders.merge(products, on="product_id", how="left")
orders_products["Order_Value"] = orders_products["quantity"] * orders_products["unit_price"]

combined_all = orders.merge(customer, on="customer_id", how="left") \
                     .merge(products, on="product_id", how="left")

combined_all["Order_Value"] = combined_all["quantity"] * combined_all["unit_price"]

final_df = combined_all[[
    "order_id", "customer_name", "product_name", "category", "quantity", "Order_Value", "region"
]]

orders_payments = combined_all.merge(payment, on="order_id", how="left")

# ----------------------------------------------------------------------------------------------------
# Identify High Value Customers (Total Purchase > 20,000)
# ----------------------------------------------------------------------------------------------------

customer_value = orders_payments.groupby(["customer_id", "customer_name", "city"])["Order_Value"].sum().reset_index()
high_value_customers = customer_value[customer_value["Order_Value"] > 20000]

print("\nHigh Value Customers (Order_Value > 20000):")
print(high_value_customers[["customer_name", "city", "Order_Value"]])

# ----------------------------------------------------------------------------------------------------
# Payment Mode Usage Count (Finance Team Requirement)
# ----------------------------------------------------------------------------------------------------

payment_mode_usage = orders_payments.groupby("payment_mode")["order_id"].count().reset_index(name="order_count")

print("\nOrders Count by Payment Mode:")
print(payment_mode_usage)

# ----------------------------------------------------------------------------------------------------
# Top Selling Product per Region (Based on Total Quantity)
# ----------------------------------------------------------------------------------------------------
product_sales_region = orders_payments.groupby(["region", "product_id", "product_name"])["quantity"].sum().reset_index()

# find top product per region
top_products = product_sales_region.sort_values(["region", "quantity"], ascending=[True, False]).groupby("region").head(1)

print("\nTop Selling Product by Region:")
print(top_products)

# ----------------------------------------------------------------------------------------------------
# Products Ordered but Payment is Pending
# ----------------------------------------------------------------------------------------------------
pending_product_orders = orders_payments[orders_payments["payment_status"] == "Pending"]

print("\nProducts that were ordered but payment pending:")
print(pending_product_orders[["product_name", "order_id", "payment_status"]])


# ----------------------------------------------------------------------------------------------------
# 20. Region summary: total_orders, completed_orders, pending_orders, total_revenue
# ----------------------------------------------------------------------------------------------------

summary = orders_payments.groupby("region").agg(
    total_orders=("order_id", "count"),
    completed_orders=("payment_status", lambda x: (x == "Completed").sum()),
    pending_orders=("payment_status", lambda x: (x == "Pending").sum()),
    total_revenue=("Order_Value", lambda x: x[orders_payments["payment_status"] == "Completed"].sum())
).reset_index()

print("\nFinal Region Summary:")
print(summary)