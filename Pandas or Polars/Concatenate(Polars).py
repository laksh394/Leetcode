# DataFrame df1
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# DataFrame df2
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# Write a solution to concatenate these two DataFrames vertically into one DataFrame.

import polars as pl

def concatenateTables(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
  return pl.concat([df1, df2], how="vertical")

# For horizontal
# return pl.concat([df1, df2], how="horizontal")
