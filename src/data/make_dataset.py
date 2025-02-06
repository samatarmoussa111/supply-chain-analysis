import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------

df = pd.read_csv("../../data/raw/supply_chain_data.csv")
df.describe()
df.isna().sum()

# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------
df.to_pickle("../../data/interim/supply_chain_data.pkl")