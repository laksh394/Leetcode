# DataFrame products
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | quantity    | int    |
# | price       | int    |
# +-------------+--------+
# Write a solution to fill in the missing value as 0 in the quantity column.

import polars as pl

def fillMissingValues(products: pl.DataFrame) -> pl.DataFrame:
  products = products.with_columns(
    pl.col("quantity").fill_null(0)
  )
  return products

# For all the columns
# products = products.fill_null(0)
