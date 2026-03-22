from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Smart Tools Hub</h1><a href='/profit'>Profit Calculator</a>"

@app.route("/profit")
def profit():
    return render_template("profit.html")

if __name__ == "__main__":
    app.run(debug=True)