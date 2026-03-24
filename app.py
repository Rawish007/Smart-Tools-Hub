from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Profit Calculator
@app.route("/profit")
def profit():
    return render_template("profit.html")

# Currency Converter
@app.route("/currency")
def currency():
    return render_template("currency.html")

# Unit Converter
@app.route("/unit")
def unit():
    return render_template("unit.html")

# Loan Calculator
@app.route("/loan")
def loan():
    return render_template("loan.html")

# Image Compressor Tool
@app.route("/image-compressor", methods=["GET", "POST"])
def image_compressor():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            img = Image.open(file)
            img = img.convert("RGB")
            
            # Save compressed image
            output_path = "compressed.jpg"
            img.save(output_path, optimize=True, quality=50)

            return send_file(output_path, as_attachment=True)

    return render_template("image.html")

# Run App
if __name__ == "__main__":
    app.run(debug=True)
