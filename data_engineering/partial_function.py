import time

import pandas as pd


def long_crunching_task(df: pd.DataFrame, offset: int) -> pd.DataFrame:
    time.sleep(30)
    df["C"] = df["A"] + df["B"] + offset  # imaginary non-vectorizational operation >_<
    return df
