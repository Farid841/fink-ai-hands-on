"""Turn the 4 files downloaded from fink-science into data/alerts.parquet.

Put the 4 part-*.parquet files in a folder called datatest/, then run:

    python prepare_data.py
"""
import glob
import os

import pandas as pd

files = sorted(glob.glob("datatest/part-*.parquet"))
if not files:
    raise SystemExit("No file found in datatest/: download the 4 part-*.parquet files first.")

alerts = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)

# a few alerts have no history: use an empty list instead of None
alerts["prv_candidates"] = alerts["prv_candidates"].apply(lambda p: [] if p is None else list(p))

os.makedirs("data", exist_ok=True)
alerts[["objectId", "candid", "candidate", "prv_candidates", "cdsxmatch"]].to_parquet("data/alerts.parquet")
print(len(alerts), "alerts saved in data/alerts.parquet")
