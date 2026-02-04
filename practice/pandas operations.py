import pandas as pd

def create_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [28, 25, 23],
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

def filtering_data_condition(df):
    print(df[df["Age"] > 23])

def filtering_multi_condi(df):
    print(df[(df["Age"] > 23) & (df["City"] == "Chennai")] )

def adding_new_columns(df):
    df["Salary"] = [50000, 60000, 70000]
    # print(df)
    return df

def updating_values(df):
    df.loc[2, "Age"] = 23
    print(df)

def droping_columns(df):
    df.drop("Salary", axis=1, inplace=True)
    print(df)

def sorting_data(df):
    return df.sort_values("Age")


if __name__ == "__main__":
    # Driver code
    df = create_dataframe()
    df = sorting_data(df)
    df.to_csv("practice/resources/output.csv", index = False)