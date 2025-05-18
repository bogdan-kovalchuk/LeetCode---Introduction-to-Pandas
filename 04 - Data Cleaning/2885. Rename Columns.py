import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Option 1
    students.columns = ["student_id", "first_name", "last_name", "age_in_years"]

    # Option 2
    students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        },
        inplace=True,
    )
    return students
