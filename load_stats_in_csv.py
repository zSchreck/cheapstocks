import requests
from download_symbols import load_symbols_from_file
import json

symbols = load_symbols_from_file()

iex_api_prefix = 'https://api.iextrading.com/1.0'


def load_stats_in_csv():
    csv = prepare_csv()
    symbols_string = ''
    for n in range(len(symbols)):
        symbols_string += symbols[n]
        symbols_string += ','
        if n % 100 == 0 and n > 0: # max of 100 stocks per api request
            query_string = iex_api_prefix + '/stock/market/batch?symbols=' + symbols_string + '&types=quote'
            response = requests.get(query_string).content
            json_format = json.loads(response)
            for key, value in json_format.iteritems():
                value = value['quote']
                if value['peRatio'] is None:
                    value['peRatio'] = 0
                if value['marketCap'] < 10000000:
                    continue
                csv.write("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(key, value['companyName'],
                                                                         value['close'], value['sector'],
                                                                         value['avgTotalVolume'], value['marketCap'],
                                                                         value['peRatio'], value['week52High'],
                                                                         value['week52Low']))
            symbols_string = ''
    csv.close()


def prepare_csv():
    open("cashmoney.csv", "w").close()
    csv = open("cashmoney.csv", "w")
    csv.write("symbol,company,price,sector,avg_volume,market_cap,pe_ratio,week52high,week52low\n")
    return csv


if __name__ == '__main__':
    load_stats_in_csv()
