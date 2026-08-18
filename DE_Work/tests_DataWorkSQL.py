import unittest
import pandas as pd

from DataWorkSQL import(
    remove_null_text_rows,
    remove_duplicates,
    clean_date_column,
    date_diff
)


#Define the test

class TestDataWorkSQL(unittest.TestCase):
    
    def test_remove_null(self):
        df = pd.DataFrame({
            "Books": [
                "HP",
                None,
                "",
                "nan",
                "LOTR"
            ]
        })

        result = remove_null_text_rows(df, "Books")
        self.assertEqual(len(result),2)


    def test_remove_dups(self):
        df = pd.DataFrame({
            "Books": [
                "Book A",
                "Book B"
                "Book B"
            ]
        })

        result = remove_duplicates(df)
        self.assertEqual(len(result),2)

    def test_clean_date_column(self):
        df =pd.DataFrame({
            "Book checkout":[
                '"01/01/2024"',
                '"15/01/2024"'
            ]
        })

        result = clean_date_column(df, "Book checkout")
        self.assertTrue(
            pd.api.types.is_datetime64_any_dtype(
                result["Book checkout"]
            )
        )

    def test_date_diff(self):
        df = pd.DataFrame({
            "Book Checkout": pd.to_datetime(
                ["15/01/2024"],
                dayfirst=True
            ),
            "Book Returned": pd.to_datetime(
                ["01/01/2024"],
                dayfirst=True
            )
        })

        result = date_diff(
            df,
            "Book Checkout",
            "Book Returned",
            "Days Borrowed"
        )

        self.assertEqual(
            result["Days Borrowed"].iloc[0],
            14
        )



if __name__ == "__main__":
    unittest.main()
        