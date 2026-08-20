# import liabry and load in the files
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from datetime import datetime
import uuid

# DE metrics to measure pipeline (userID and DateTime)
run_id = str(uuid.uuid4())
run_timestamp = datetime.now()

# Extract
Systembook = pd.read_csv("03_Library Systembook.csv")
Customer = pd.read_csv("03_Library SystemCustomers.csv")

# DE metrics to measure pipeline (track rows removed durring cleaning)
SB_row_before_cleaning = len(Systembook)
C_row_before_cleaning = len(Customer)

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

# DE metrics to measure pipeline (track rows removed durring cleaning)
SB_nulls_removed = SB_row_before_cleaning - len(Systembook)
C_nulls_removed = C_row_before_cleaning - len(Customer)

## Function Remove Duplicates
def remove_duplicates(df):
    return df.drop_duplicates()

### use

# Track rows before duplicate removal
SB_rows_before_duplicates = len(Systembook)
Systembook = remove_duplicates(Systembook)

C_rows_before_duplicates = len(Customer)
Customer = remove_duplicates(Customer)

# DE metrics to measure pipeline (track rows removed durring cleaning)
SB_duplicates_removed = (
    SB_rows_before_duplicates - len(Systembook)
)

C_duplicates_removed = (
    C_rows_before_duplicates - len(Customer)
)

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

# DE metrics to measure pipeline (track dates)
SB_invalid_checkout_dates = Systembook["Book checkout"].isna().sum()

SB_invalid_return_dates = Systembook["Book Returned"].isna().sum()

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

# DE metrics to measure pipeline (invalid borrowing periods)

SB_negitive_days_borrowed = (
    Systembook["Days Borrowed"] < 0
).sum()

# DE metrics to measure pipeline (dropped records)

SB_book_records_loaded = len(Systembook)

SB_book_records_dropped = (
    SB_row_before_cleaning - SB_book_records_loaded
)

C_customer_records_loaded = len(Customer)

C_customer_records_dropped = (
    C_row_before_cleaning - C_customer_records_loaded
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

# DE metrics to measure pipeline (customer referential integrity)

Missing_customer_ids = (
    ~Systembook["Customer ID"].isin(Customer["Customer ID"])
).sum()



# DE metrics table

metrics_data = [
    ["SystemBook", "RowsReceived", SB_row_before_cleaning],
    ["SystemBook", "RowsLoaded", SB_book_records_loaded],
    ["SystemBook", "RowsDropped", SB_book_records_dropped],
    ["SystemBook", "NullsRemoved", SB_nulls_removed],
    ["SystemBook", "DuplicatesRemoved", SB_duplicates_removed],
    ["SystemBook", "InvalidCheckoutDates", SB_invalid_checkout_dates],
    ["SystemBook", "InvalidReturnDates", SB_invalid_return_dates],
    ["SystemBook", "InvalidDaysBorrowed", SB_negitive_days_borrowed],
    ["SystemBook", "MissingCustomerID", Missing_customer_ids],


    ["Customer", "RowsReceived", C_row_before_cleaning],
    ["Customer", "RowsLoaded", C_customer_records_loaded],
    ["Customer", "RowsDropped", C_customer_records_dropped],
    ["Customer", "NullsRemoved", C_nulls_removed],
    ["Customer", "DuplicatesRemoved", C_duplicates_removed]
]

PipelineMetrics = pd.DataFrame(
    metrics_data,
    columns=["Source", "Metric", "Value"]
)

PipelineMetrics["RunID"] = run_id
PipelineMetrics["RunTimestamp"] = run_timestamp

# Reorder columns
PipelineMetrics = PipelineMetrics[
    ["RunID", "RunTimestamp", "Source", "Metric", "Value"]
]

PipelineMetrics.to_sql(
    "Pipeline_Metrics",
    engine,
    if_exists="append",
    index=False
)

print("ETL completed successfully.")