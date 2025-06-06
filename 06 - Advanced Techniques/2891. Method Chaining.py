import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    mask = animals["weight"] > 100
    filtered = animals[mask]
    sorted = filtered.sort_values(by="weight", ascending=False)
    return sorted[["name"]]
