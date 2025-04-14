# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.
# Write a solution to remove the rows with missing values.

import polars as pl

def dropMissingNames(students: pl.DataFrame) -> pl.DataFrame:
    return students.filter(pl.col("name").is_not_null())
