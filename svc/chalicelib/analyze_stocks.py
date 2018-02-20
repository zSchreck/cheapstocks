import pandas as pd
from sys import argv
import json


def get_data_single_stock(stocksymbol):
    stocksymbol = stocksymbol.upper()
    df = pd.read_csv("./chalicelib/data_files/cashmoney.csv")
    stock_data = dict()
    stock = df.loc[(df['symbol'] == stocksymbol)].values[0]
    stock_data['symbol'] = stock[0]
    stock_data['company_name'] = stock[1]
    stock_data['price'] = stock[2]
    stock_data['sector'] = stock[3]
    stock_data['avg_volue'] = stock[4]
    stock_data['market_cap'] = stock[5]
    stock_data['pe_ratio'] = stock[6]
    stock_data['week52high'] = stock[7]
    stock_data['week52low'] = stock[8]
    return stock_data


def build_stock_dict(stocksymbol, stock_data):
    dumped_str = json.dumps({stocksymbol: stock_data})
    return dumped_str


def get_data_batch_stocks(stocksymbols):
    stocks_data = dict()
    for stock in stocksymbols:
        stocks_data[stock] = get_data_single_stock(stock)
    return json.dumps(stocks_data)



#
# if __name__ == '__main__':
#     df = pd.read_csv("./data_files/cashmoney.csv")
#     high_pe = 10
#     market_cap = 250000000
#     stock = None
#     if len(argv) > 1:
#         try:
#             for n in range(len(argv) - 1):
#                 if argv[n + 1] == '-s':
#                     stock = argv[n + 2].upper()
#                     break
#                 if argv[n + 1] == '-pe':
#                     high_pe = float(argv[n + 2])
#                 if argv[n + 1] == '-mc':
#                     market_cap = float(argv[n + 2])
#         except (IndexError, ValueError):
#             print "Invalid arguments passed to function. Please refer to README.md for instructions."
#             exit()
#     # print rows where pe ratio is between 0 and 'high_pe' and market cap is above 'market_cap'
#     if stock:
#         print df.loc[(df['symbol'] == stock)]
#     else:
#         print df.loc[(df['pe_ratio'] > 0) & (df['pe_ratio'] < high_pe) & (df['market_cap'] > market_cap)]
#
#
