import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("cashmoney.csv")
    # print rows where pe ratio is between 0 and 10 and market cap is above 250 million
    print df.loc[(df['pe_ratio'] > 0) & (df['pe_ratio'] < 10) & (df['market_cap'] > 250000000)]


