# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# | grade       | float  |
# +-------------+--------+
# Write a solution to correct the errors:
# The grade column is stored as floats, convert it to integers.

import polars as pl

def changeDatatype(students: pl.DataFrame) -> pl.DataFrame:
  students = students.with_columns(
    pl.col("grade").cast(pl.Int64)
  )
  return students
