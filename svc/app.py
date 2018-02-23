from chalice import Chalice
from chalice import BadRequestError
from chalicelib import analyze_stocks
import json
app = Chalice(app_name="cheapstocks")


@app.route("/test")
def test():
    return {"hello": "world"}


@app.route("/v0/stocksymbol/{stocksymbol}", methods=['GET'])
def get_data_for_single_stock(stocksymbol):
    if stocksymbol is None:
        raise BadRequestError("Stock symbol passed was null")
    stocksymbol = stocksymbol.upper()
    dumped_str = analyze_stocks.build_stock_dict(stocksymbol, analyze_stocks.get_data_single_stock(stocksymbol))
    return json.loads(dumped_str)


@app.route("/v0/stocksymbols/{stocksymbols}", methods=['GET'])
def get_data_for_batch_stocks(stocksymbols):
    if stocksymbols is None:
        raise BadRequestError("Stock symbol passed was null")
    dumped_str = analyze_stocks.get_data_batch_stocks(stocksymbols.split(','))
    return json.loads(dumped_str)


@app.route("/v0/peratio/{peratio}/marketcap/{marketcap}", methods=['GET'])
def get_data_by_pe_mkcap(peratio, marketcap):
    dumped_str = analyze_stocks.get_data_pe_mkcap(float(peratio), int(marketcap))
    return json.loads(dumped_str)


@app.route("/v0/peratio/{peratio}", methods=['GET'])
def get_data_by_pe(peratio):
    dumped_str = analyze_stocks.get_data_pe_mkcap(float(peratio), None)
    return json.loads(dumped_str)


@app.route("/v0/marketcap/{marketcap}", methods=['GET'])
def get_data_by_mkcap(marketcap):
    dumped_str = analyze_stocks.get_data_pe_mkcap(None, int(marketcap))
    return json.loads(dumped_str)


@app.route("/v0/alldata", methods=['GET'])
def get_data_for_all_stocks():
    dumped_str = analyze_stocks.get_data_pe_mkcap(None, None)
    return json.loads(dumped_str)
