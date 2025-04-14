# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# +------------+---------+-----+
# Write a solution to select the name and age of the student with student_id = 101.

import polars as pl

def selectData(students: pl.DataFrame) -> pl.DataFrame:
    return students.filter(pl.col("student_id") == 101).select(pl.col(["name", "age"]))
