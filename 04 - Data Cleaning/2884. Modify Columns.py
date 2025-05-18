import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Option 1
    employees["salary"] = employees["salary"] * 2

    # Option 2
    employees.salary *= 2

    return employees
