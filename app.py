from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profit")
def profit():
    return render_template("profit.html")

@app.route("/currency")
def currency():
    return render_template("currency.html")

@app.route("/unit")
def unit():
    return render_template("unit.html")

@app.route("/loan")
def loan():
    return render_template("loan.html")

if __name__ == "__main__":
    app.run(debug=True)