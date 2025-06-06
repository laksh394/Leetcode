# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | id          | int    |
# | first       | object |
# | last        | object |
# | age         | int    |
# +-------------+--------+
# Write a solution to rename the columns as follows:
# id to student_id
# first to first_name
# last to last_name
# age to age_in_years

import polars as pl

def renameColumns(students: pl.DataFrame) -> pl.DataFrame:
  return students.rename({"id":"student_id", "first":"first_name", "last":"last_name", "age":"age_in_years"})
