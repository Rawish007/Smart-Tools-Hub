from flask import Flask, render_template, request, send_file
from PIL import Image
import os

@app.route("/image-compressor", methods=["GET", "POST"])
def image_compressor():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            img = Image.open(file)
            img = img.convert("RGB")
            img.save("compressed.jpg", optimize=True, quality=50)
            return send_file("compressed.jpg", as_attachment=True)
    return render_template("image.html")
