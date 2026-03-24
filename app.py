from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)

# HOME
@app.route("/")
def home():
    return render_template("index.html")

# TOOLS
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
