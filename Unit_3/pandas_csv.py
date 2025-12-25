import pandas as pd

df = pd.read_csv('sales_r.csv')

print(df.shape) # Inspection
print(df.columns)
print(df.index) # Shows the numbering of rows
print(df.dtypes) # Shows the data types of individual columns
print(df.head(3)) # To display n number of records
print(df.tail(3)) # To display n number of records from last

# ------- Preprocessing of data ---------------
# Check for NaN Values in columns
print(df.isna())
print(df.isna().sum())

# Check for NaN Values in rows
print(df.isna().any(axis = 1))

print(df.isna().any(axis = 1).sum()) # 8

# Check for not NaN Values in columns
print(df.notna())
print(df.notna().sum())

# Check for not NaN Values in rows
print(df.notna().any(axis = 1))
print(df.notna().any(axis = 1).sum()) # 10

# Clean the column names
df.columns = df.columns.str.strip()
print(df.columns)

print(df.head)
# Remove quotes, commas from a particular column
# Step 1: Convert column amount to str
# Step 2: Replace quotes
# Step 3: Replace comma
# Step 4: Extract the numeric digits

df['Amount'] = (
    df['Amount'].astype(str)
    .str.replace('"','',regex = False)
    .str.replace(',','',regex = False)
    .str.extract(r'(\d+)',expand = False)
)
print(df.dtypes)

print(df['Amount'])

# Nan values can be replaced with
# 1. median - mid value
# 2. mean - average value
# 3. mode - value that has highest frequency
# Only if the column is numeric

# Convert column to numeric
df['Amount'] = pd.to_numeric(df['Amount'], errors= 'coerce')
'''First parameter - column that has to be converted
   errors = coerce (all non-numeric characters will be converted as NaN)'''
print(df.dtypes)

# Fill NaN values with median
df['Amount'] = df['Amount'].fillna(df['Amount'].median())
print(df['Amount'])
print(df['Qty'])

# Replace space in Qty with mean
df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')
print(df.dtypes)
print(df['Qty'])

# Fill Qty's NaN values with mean
df['Qty'] = df['Qty'].fillna(df['Qty'].mean())
print(df['Qty'])
print(df.head)

# Drop Columns
# 1. If the column contains too many NaN
# 2. If it is an unwanted column

df = df.dropna(axis=1, how = 'all')
print(df.columns) # Still there are 6 unnamed

df = df.dropna(axis=1, how = 'any')
print(df.columns)

# Equivalent commands
# df = df.drop(columns=['Unnamed: 6'])

# Drop columns given the exact name of the column
# df = df.iloc[:,:-1]
# df = df.loc[:,~df.columns.str.contains('^Unnamed')]

# print(df['Region'])

# Standardize Text Columns
df['Region'] = df['Region'].str.strip().str.lower()

print(df['Region'])

# Remove quotes in all columns
df = df.apply(lambda c : c.astype(str).str.replace('"','',regex = False))
print(df)

# 1. Convert the Region to numeric. All non-numeric values become NaN
# 2. Create a boolean mask. It is True when Region is 500 or 800
# 3. Replace all such rows with Region as North

df.loc[pd.to_numeric(df['Region'],errors='coerce')
            .isin([500,800]), 'Region']= 'north'
print(df)

# Filter data based on conditions
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
hsales = df['Amount'] > 2000

print(type(hsales))
print(hsales)

# Create a data frame based on the filter
df_high = df[hsales]
print(type(df_high))
print(df_high)

# To count the number of records or rows in a Dataframe 
# print(len(df)) # 10
# print(len(df_high)) # 4

# Filtering based on multiple conditions
c_amt = df['Amount']>2000
c_reg = df['Region'] == 'south'
print(type(c_amt), type(c_reg))

# Conditions can be & or |
df_t1 = df[c_amt & c_reg]
df_t2 = df[c_amt | c_reg]
df_t3 = df[c_reg | c_amt]
df_t4 = df[c_reg & c_amt]
print(len(df_t1), len(df_t2))
print(len(df_t3), len(df_t4))

print(df_t1)

# Sort the values in column
df_sort = df.sort_values('Amount')
print('\n',df_sort)
df_desc = df.sort_values('Amount', ascending = False)
print('\n',df_desc)

df_s1 = df.sort_values(['Region', 'Amount'])
print('\n',df_s1)

df_s2 = df.sort_values(['Region', 'Amount'], ascending = [True, False]) # Region - Ascending, Amount  - Descending
print('\n',df_s2)

# Create new columns based on existing columns

df['Tax'] = df['Amount']*0.18
print(df.columns)
print(df.dtypes)
print(df)

df['Total_Tax'] = df['Amount'] + df['Tax']
print('\n',df['Total_Tax'])

# ------- Profiling the columns ----------
# 1. Count the values
print(df['Region'].value_counts())
print()
print(df['Amount'].value_counts())

# 2. Summarize the data frame
print(df['Amount'].describe())
print()
print(df['Region'].describe())
print()
print(df['City'].describe())
print()

# 3. Grouping the data
grp_reg = df.groupby('Region')
print(type(grp_reg), len(grp_reg), grp_reg)

# ------ View the grouped data ------
# 1. View thw group names
print(grp_reg.groups.keys())

# 2. View the row index that belongs to each group
print(grp_reg.groups)

# 3. View specific group
print()
print(grp_reg.get_group('north'))

# 4. Loop through all the groups 
for n, g in grp_reg:
    print(f'Group: {n}')
    print(g)

# Grouping based on multiple columns
grp_mul = df.groupby(['Region', 'City'])
print()
print(grp_mul.groups)
print()

# Sum of the amount af each region
sales_reg = grp_reg['Amount'].sum()
print(sales_reg)
print()

# Multiple Aggression
region_summary = grp_reg['Amount'].agg(['sum', 'mean', 'count'])
print(region_summary)

# Custom Aggression
summary = df.groupby('Region').agg(
    Total_Amt = ('Amount', 'sum'),
    Avg_Amt = ('Amount', 'mean'), 
    Avg_Tax = ('Tax', 'mean'),
    Unique_City = ('City', 'nunique') 
)
print(type(summary)) # <class 'pandas.core.frame.DataFrame'>
print()
print(summary)