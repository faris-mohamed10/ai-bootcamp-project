from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from helpers.detect import detect_image_class

# Initializing flask application
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def home():
    return render_template('form.html', title='Home')


@app.route("/predict", methods=["POST"])
def processReq():
    data = request.files["img"]
    data.save("img.jpg")

    result = detect_image_class("img.jpg")

    return render_template("result.html", result_image=result)
