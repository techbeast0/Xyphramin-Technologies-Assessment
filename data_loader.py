import pandas as pd

def load_and_prepare_data(filepath: str) -> pd.DataFrame:
    
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.sort_values(by='Date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

# Load all files
filepaths = {
    "NVDA": "data/NVDA_2005_2023.csv",
    "QQQ": "data/QQQ_2005_2023.csv",
    "SOXS": "data/SOXS_2005_2023.csv"
}

datasets = {name: load_and_prepare_data(path) for name, path in filepaths.items()}