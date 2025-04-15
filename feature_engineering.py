import pandas as pd

def compute_volatility(df: pd.DataFrame) -> pd.DataFrame:
    
    df['Volatility'] = (df['High'] - df['Low']) / df['Close']
    df['Volume_delta'] = df['Volume'].diff()
    df['Volatility_delta'] = df['Volatility'].diff()
    df.dropna(inplace=True)
    return df[['Date', 'Volume_delta', 'Volatility_delta']]