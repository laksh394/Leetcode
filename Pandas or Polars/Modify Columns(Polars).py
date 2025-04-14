# DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+
# A company intends to give its employees a pay rise.
# Write a solution to modify the salary column by multiplying each salary by 2.

import polars as pl

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.with_columns((pl.col("salary") * 2).alias("salary"))
    return employees
