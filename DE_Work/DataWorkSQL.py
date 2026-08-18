# import liabry and load in the files

import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

Systembook = pd.read_csv("03_Library Systembook.csv")

Customer = pd.read_csv("03_Library SystemCustomers.csv")

# Clean up (Remove Null, Remove duplicates, format columns)

## Function Remove Null
def remove_null_text_rows(df, column):
    return df[
        (df[column].notna()) &
        (df[column].astype(str).str.strip().str.lower() != "nan") &
        (df[column].astype(str).str.strip() != "")
    ]

### use
Systembook = remove_null_text_rows(Systembook, "Books")
Customer = remove_null_text_rows(Customer, "Customer Name")

## Function Remove Duplicates
def remove_duplicates(df):
    return df.drop_duplicates()

### use
Systembook = remove_duplicates(Systembook)
Customer = remove_duplicates(Customer)


## Remove the "" from date
Systembook["Book checkout"] = (
    Systembook["Book checkout"]
    .astype(str)
    .str.replace('"', '', regex=False)
    .str.strip()
)

## Function Format Date
def clean_date_column(df, column):
    df[column] = (
        df[column]
        .astype(str)
        .str.replace('"', '', regex=False)
        .str.strip()
    )

    df[column] = pd.to_datetime(
        df[column],
        dayfirst=True,
        errors="coerce"
    )

    return df

### use

Systembook = clean_date_column(
    Systembook,
    "Book checkout"
)

Systembook = clean_date_column(
    Systembook,
    "Book Returned"
)

## Function to calcualte the differnece bewteen the two date columns

def date_diff(df, start_col, end_col, new_col):
    df[new_col] = (df[end_col] - df[start_col]).dt.days
    return df

### use
Systembook = date_diff(
    Systembook,
    "Book checkout",
    "Book Returned",
    "Days Borrowed"
)

# Save to SQL
##Connect
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=DataEngineering;"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={quote_plus(conn_str)}"
)

##Save Tables
Systembook.to_sql(
    "Systembook_Clean",
    engine,
    if_exists="replace",
    index=False
)

Customer.to_sql(
    "Customer_Clean",
    engine,
    if_exists="replace",
    index=False
)

print("ETL completed successfully.")
