# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+
# A company plans to provide its employees with a bonus.
# Write a solution to create a new column name bonus that contains the doubled values of the salary column.

import polars as pl

def createBonusColumn(employees: pl.DataFrame) -> pl.DataFrame:
    return employees.with_columns((pl.col("salary"))*2).alias("bonus)
