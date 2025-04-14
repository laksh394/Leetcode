# DataFrame customers
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | customer_id | int    |
# | name        | object |
# | email       | object |
# +-------------+--------+
# There are some duplicate rows in the DataFrame based on the email column.
# Write a solution to remove these duplicate rows and keep only the first occurrence.

import polars as pl

def dropDuplicateEmails(customers: pl.DataFrame) -> pl.DataFrame:
    return customers.unique(subset=["email"])
