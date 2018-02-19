import pandas as pd
from sys import argv

if __name__ == '__main__':
    df = pd.read_csv("./data_files/cashmoney.csv")
    high_pe = 10
    market_cap = 250000000
    stock = None
    if len(argv) > 1:
        try:
            for n in range(len(argv) - 1):
                if argv[n + 1] == '-s':
                    stock = argv[n + 2].upper()
                    break
                if argv[n + 1] == '-pe':
                    high_pe = float(argv[n + 2])
                if argv[n + 1] == '-mc':
                    market_cap = float(argv[n + 2])
        except IndexError:
            print "Invalid arguments passed to function. Please refer to README.md for instructions."


    # print rows where pe ratio is between 0 and 'high_pe' and market cap is above 'market_cap'
    if stock:
        print df.loc[(df['symbol'] == stock)]
    else:
        print df.loc[(df['pe_ratio'] > 0) & (df['pe_ratio'] < high_pe) & (df['market_cap'] > market_cap)]


