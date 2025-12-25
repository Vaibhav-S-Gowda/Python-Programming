import pandas as pd

# --------------------------------------------------
# Read CSV files
# --------------------------------------------------
s1 = pd.read_csv('sales.csv')
s2 = pd.read_csv('sales_q2.csv')

# --------------------------------------------------
# Check whether the two DataFrames have the same structure
# --------------------------------------------------
print("Shapes:")
print(s1.shape, s2.shape)

print("\nColumns in s1:")
print(s1.columns)

print("\nColumns in s2:")
print(s2.columns)

# --------------------------------------------------
# Combine two DataFrames vertically
# --------------------------------------------------

# ignore_index=True -> resets index from 0 continuously
s_all = pd.concat([s1, s2], ignore_index=True)

# ignore_index=False (default) -> keeps original indices
s_all1 = pd.concat([s1, s2])

print("\nShapes after concatenation:")
print(s_all.shape, s_all1.shape)

# --------------------------------------------------
# Preview data
# --------------------------------------------------
print("\nHead of s_all (ignore_index=True):")
print(s_all.head())

print("\nHead of s_all1 (original indices kept):")
print(s_all1.head())

# --------------------------------------------------
# Export DataFrames
# --------------------------------------------------

# CSV export
s_all.to_csv('sales_all.csv', index=False)     # without index
s_all.to_csv('sales_all_1.csv')                # with index

# Excel export
s_all1.to_excel('sales_all.xlsx', index=False)

# JSON export
s_all.to_json('sales_all.json', index=False)
s_all.to_json('sales_all_1.json')

# XML export
s_all.to_xml('sales_all.xml', index=False, parser='etree')
s_all.to_xml('sales_all_1.xml', parser='etree')

# --------------------------------------------------
# Notes:
# index=False -> index is not written to file
# index=True  -> index is written as an extra column (default)
# --------------------------------------------------
