import os
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

    save_path = os.path.join(os.path.dirname(
        __file__), 'static/temp/test.png')

    data.save(save_path)

    result = detect_image_class(save_path)

    return render_template("result.html", result_image=result)
