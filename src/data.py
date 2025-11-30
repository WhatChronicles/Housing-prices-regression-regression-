import pandas as pd
import numpy as np
import os
def load_data(path="data/train.csv"):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    full_path = os.path.join(root_dir, path)
    df = pd.read_csv(full_path)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    if "id" in df.columns:
        df = df.drop_duplicates(subset=["id"])


    target = "saleprice"

    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in num_cols:
        if df[col].isna().mean() > 0:
            df[col] = df[col].fillna(df[col].median())

    cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()
    for col in cat_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace({"NA": np.nan, "None": np.nan})
        df[col] = df[col].fillna("Missing")

    if set(["fullbath","halfbath"]).issubset(df.columns):
        df["total_baths"] = df["fullbath"] + 0.5*df["halfbath"]
    if set(["grlivarea","totrmsabvgrd"]).issubset(df.columns):
        df["area_per_room"] = df["grlivarea"] / df["totrmsabvgrd"].replace(0, np.nan)

    if "grlivarea" in df.columns:
        upper = df["grlivarea"].quantile(0.99)
        df["grlivarea"] = df["grlivarea"].clip(upper=upper)

    return df