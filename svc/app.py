from chalice import Chalice

app = Chalice(app_name="cheapstocks")


@app.route("/")
def index():
    return {"hello": "world"}