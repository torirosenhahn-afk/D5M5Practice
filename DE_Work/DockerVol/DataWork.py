# import liabry and load in the files

import pandas as pd

Systembook = pd.read_csv("03_Library_Systembook.csv")

Customer = pd.read_csv("03_Library_SystemCustomers.csv")

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

# Save cleaned files to the Docker volume

Systembook.to_csv(
    "/data/Systembook_Clean_New.csv",
    index=False
)

Customer.to_csv(
    "/data/Customer_Clean_New.csv",
    index=False
)

print("Files saved successfully.")