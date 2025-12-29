import pickle as p
import pandas as pd

# Data Frames

data = {'Name': ['Alpha', 'Beta', 'Gamma'],
        'Age': [12, 34, 67],
        'City': ['Bangalore', 'Mangalore', 'Mysore']}

df = pd.DataFrame(data)
print(df)
print(type(df))

df.to_pickle('df.pkl')
p_df = pd.read_pickle('df.pkl')
print(p_df)
print(type(p_df))


