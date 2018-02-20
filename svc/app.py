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
    dumped_str = analyze_stocks.build_stock_dict(stocksymbol, analyze_stocks.get_data_single_stock(stocksymbol))
    return json.loads(dumped_str)


@app.route("/v0/stocksymbols/{stocksymbols}", methods=['GET'])
def get_data_for_batch_stocks(stocksymbols):
    if stocksymbols is None:
        raise BadRequestError("Stock symbol passed was null")
    return json.loads(analyze_stocks.get_data_batch_stocks(stocksymbols.split(',')))