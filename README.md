# cheapstocks
---

Python project to look at quotes from every single stock listed on the New York Stock Exchance and on the NASDAQ Exchange, and filter by certain financial criteria, like P/E Ratio, market cap, sector, volume, etc.
---
Currently only downloads data and stores it in a CSV, but will soon integrate panda for better data analysis. 

download_symbols.py downloads all available stock symbols for NYSE and NASDAQ(more exchanges can be added easily) and saves them in an alphabetically sorted text file called symbols.txt.

load_stats_in_csv.py loads all symbols from symbols.txt into a list and makes api calls to the IEX api to get requested financial information. Calls are made in batches of 100. The information is then saved into an csv file appropriately called cashmoney.csv to be analyzed in the future. 

analyze_stocks.py uses pandas to read from cashmoney.csv and return stocks with certain criteria. It defaults to a P/E Ratio between 0 and 10, and market cap above 250 million. 

Analyze stocks can take in 3 different parameters. -s takes in a string 'stock' and returns the associated data with this stock symbol if there is any. -s can not be run with any other flags. -pe takes in a number to search for stocks with a P/E ration under this number. 
-mc also takes in a number, but to search for stocks with a market cap under this number. 

An example to search for stocks with a P/E ratio under 17 with a market cap above 500 million would look like this: python analyze_stocks.py -pe 17 -mc 500000000. 

Data provided for free by [IEX](https://iextrading.com/developer)

[IEX API docs](https://iextrading.com/developer/docs/)
