import pandas as pd

def create_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [21, 22, 23],
        "City": ["Bangalore", "Chennai", "Delhi"]
    }

    df = pd.DataFrame(data)
    return df

def first_row(df):
    print(df.head())

def last_rows(df):
    print(df.tail(2))

def shape_row_col(df):
    print(df.shape)

def col_names(df):
    print(df.columns)

def info_dataTypes(df):
    print(df.info())

def selecting_single_col(df):
    print(df["Name"])

def selecting_mul_col(df):
    print(df[["Name", "City"]])

def selecting_rows_by_index(df):
    print(df.iloc[0])

def selecting_multi_row_by_index(df):
    print(df.iloc[0:2])

def sel_by_label(df):
    print(df.loc[1])

if __name__ == "__main__":
    # Driver code
    df = create_dataframe()
    sel_by_label(df)
    selecting_rows_by_index(df)