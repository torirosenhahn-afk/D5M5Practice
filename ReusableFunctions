# Remove nulls
def remove_null_text_rows(df, column):
    return df[
        (df[column].notna()) &
        (df[column].astype(str).str.strip().str.lower() != "nan") &
        (df[column].astype(str).str.strip() != "")
    ]

#use
Systembook = remove_null_text_rows(Systembook, "Books")
Customer = remove_null_text_rows(Customer, "Customer Name")


#remove duplicates

def remove_duplicates(df):
return df.drop_duplicates()

#use
Systembook = remove_duplicates(Systembook)
Customer = remove_duplicates(Customer)

#clean text

def clean_text_column(df, column):
df[column] = df[column].astype(str).str.strip()
return df

#use
Systembook = clean_text_column(Systembook, "Books")

#convert column to date

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

#use

Systembook = clean_date_column(
    Systembook,
    "Book checkout"
)

Systembook = clean_date_column(
    Systembook,
    "Book Returned"
)

#date dif

def date_diff(df, start_col, end_col, new_col):
df[new_col] = (
df[end_col] - df[start_col]
).dt.days
return df

#use
Systembook = date_diff(
    Systembook,
    "Book checkout",
    "Book Returned",
    "Days Borrowed"
)


#Complete Transformation Pipeline

def clean_systembook(df):

    df = remove_null_text_rows(df, "Books")
    df = remove_duplicates(df)

    df = clean_text_column(df, "Books")

    df = clean_date_column(df, "Book checkout")
    df = clean_date_column(df, "Book Returned")

    df = date_diff(
        df,
        "Book checkout",
        "Book Returned",
        "Days Borrowed"
    )

    return df

#use
Systembook = clean_systembook(Systembook)