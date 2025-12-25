import pandas as pd

# Create a dataframe from a dictionary
data = {'Name' : ['Amora', 'Beast', 'Captain America'],
        'Age': [25, 30, 25],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)
# print(type())
print(df)

# Create a dataframe from a list
data = [['Deadpool',25,'New York'],
        ['Elektra',24,'Paris'],
        ['Falcon',30,'London']]
df1 = pd.DataFrame(data)
print('\n', df1,'\n')
df2 = pd.DataFrame(data, columns=['Name','Age','City'])
print(df2)

# Create a dataframe from a file
# df5 = pd.read_csv('datapandas.csv')
# print('CSV \n',df5)

# df6 = pd.read_json('datapandas.json')
# print('Json\n',df6)

df7 = pd.read_excel("VideoSales.xlsx")
print(df7)

# -------------------------------
#      Inspection Mothods
# -------------------------------

print(df7.head())
print(df7.tail())
print(df7.loc[0:3])
print(df7.loc[5:9,['Name','Genre']])

print(df7.isna().any(axis=1).sum())  # Check for missing values
print(df7.info())  # Summary of the dataframe
print(df7.describe())  # Statistical summary of numerical columns

print(df7.notna())