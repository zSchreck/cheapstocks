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


def get_data_pe_mkcap(peratio, marketcap):
    df = pd.read_csv("./chalicelib/data_files/cashmoney.csv")

    if peratio is not None and marketcap is not None:
        stocks = df.loc[(df['pe_ratio'] > 0) & (df['pe_ratio'] < peratio) & (df['market_cap'] > marketcap)].values
    elif peratio is not None and marketcap is None:
        stocks = df.loc[(df['pe_ratio'] > 0) & (df['pe_ratio'] < peratio)].values
    elif peratio is None and marketcap is not None:
        stocks = df.loc[df['market_cap'] > marketcap].values
    else:
        stocks = df.values

    stocks_data = dict()
    for stock in stocks:
        symbol = stock[0]
        stocks_data[symbol] = get_data_single_stock(symbol)
    return json.dumps(stocks_data)

