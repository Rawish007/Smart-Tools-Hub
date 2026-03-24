from flask import Flask, render_template, request, send_file
from PIL import Image
import random
import string
from datetime import datetime

app = Flask(__name__)

# HOME
@app.route("/")
def home():
    return render_template("index.html")

# PROFIT
@app.route("/profit")
def profit():
    return render_template("profit.html")

# CURRENCY
@app.route("/currency")
def currency():
    return render_template("currency.html")

# UNIT
@app.route("/unit")
def unit():
    return render_template("unit.html")

# LOAN
@app.route("/loan")
def loan():
    return render_template("loan.html")

# IMAGE COMPRESSOR
@app.route("/image-compressor", methods=["GET", "POST"])
def image_compressor():
    if request.method == "POST":
        file = request.files["image"]
        img = Image.open(file)
        path = "compressed.jpg"
        img.save(path, optimize=True, quality=30)
        return send_file(path, as_attachment=True)
    return render_template("image.html")

# AGE CALCULATOR
@app.route("/age", methods=["GET", "POST"])
def age():
    result = ""
    if request.method == "POST":
        birth = request.form["birth"]
        today = datetime.today()
        birth_date = datetime.strptime(birth, "%Y-%m-%d")
        age = today.year - birth_date.year
        result = f"Your age is {age} years"
    return render_template("age.html", result=result)

# PASSWORD GENERATOR
@app.route("/password")
def password():
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(10))
    return render_template("password.html", password=password)

# BMI CALCULATOR
@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    result = ""
    if request.method == "POST":
        w = float(request.form["weight"])
        h = float(request.form["height"]) / 100
        bmi = w / (h*h)
        result = f"Your BMI is {round(bmi,2)}"
    return render_template("bmi.html", result=result)

# EXTRA PAGES
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

if __name__ == "__main__":
    app.run(debug=True)
