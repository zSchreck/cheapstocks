# cheapstocks
---

Python project to look at quotes from every single stock listed on the New York Stock Exchange and on the NASDAQ Exchange, and filter by certain financial criteria, like P/E Ratio, market cap, sector, volume, etc.
---
Currently only downloads data and stores it in a CSV, but will soon integrate panda for better data analysis. 

download_symbols.py downloads all available stock symbols for NYSE and NASDAQ(more exchanges can be added easily) and saves them in an alphabetically sorted text file called symbols.txt.

load_stats_in_csv.py loads all symbols from symbols.txt into a list and makes api calls to the IEX api to get requested financial information. Calls are made in batches of 100. The information is then saved into an csv file appropriately called cashmoney.csv to be analyzed in the future. 

analyze_stocks.py uses pandas to read from cashmoney.csv and return stocks with certain criteria. It defaults to a P/E Ratio between 0 and 10, and market cap above 250 million. 

This is a chalice app that currently has three endpoints, '/test' just returns hello world and is used to make sure the app is up and running, '/v0/stocksymbol/{stocksymbol}' takes in a single stock ticker and returns information about that stock, and 'v0/stocksymbols/{stocksymbols}' takes in a comma separated list of stock tickers and returns information about those stocks. '/v0/peratio/{peratio}/marketcap/{marketcap}' returns stocks that are under P/E ratio peratio, and above Market Cap marketcap.

Data provided for free by [IEX](https://iextrading.com/developer)

[IEX API docs](https://iextrading.com/developer/docs/)
