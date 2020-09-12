import flask
import scraper

ticker = "ATL"

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/statements', methods=['GET'])
def statements():
    return scraper.get_financial_statements(ticker)

@app.route('/metrics', methods=['GET'])
def metrics():
    return scraper.get_metrics(ticker)

@app.route('/profile', methods=['GET'])
def profile():
    return scraper.get_profile(ticker)

app.run()
