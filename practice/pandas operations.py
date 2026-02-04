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

if __name__ == "__main__":
    # Driver code
    df = create_dataframe()
    shape_row_col(df)