# cheapstocks
---

Python project to look at quotes from every single stock listed on the New York Stock Exchance and on the NASDAQ Exchange, and filter by certain financial criteria, like P/E Ratio, market cap, sector, volume, etc.
---
Currently only downloads data and stores it in a CSV, but will soon integrate panda for better data analysis. 

download_symbols.py downloads all available stock symbols for NYSE and NASDAQ(more exchanges can be added easily) and saves them in an alphabetically sorted text file called symbols.txt.

load_stats_in_csv.py loads all symbols from symbols.txt into a list and makes api calls to the IEX api to get requested financial information. Calls are made in batches of 100. The information is then saved into an csv file appropriately called cashmoney.csv to be analyzed in the future. 


Data provided for free by [IEX](https://iextrading.com/developer)

[IEX API docs](https://iextrading.com/developer/docs/)
