#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request, Response
from flask_cors import CORS
import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO
from imageprocess import image_process


img_process = image_process()

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def hello():
    return 'test'

@app.route("/img", methods=["POST"])
def img():
    img_base64 = request.form['image']
    code = base64.b64decode(img_base64.split(',')[1]) 
    imgPIL = Image.open(BytesIO(code))
    imgCV = np.asarray(imgPIL)

    # img_process.image_process(imgCV)
    imgCV = cv2.resize(imgCV, (640, 360))
    imgCV = cv2.cvtColor(imgCV, cv2.COLOR_BGR2GRAY)
    ret, bin = cv2.threshold(imgCV, 0, 255, cv2.THRESH_OTSU)
    imgCV = cv2.bitwise_not(bin)
    

    ret, png_data = cv2.imencode(".png", imgCV)
    # img_bytes = BytesIO(imgCV)
    imgCV_base64 = base64.b64encode(png_data).decode()

    return f"data:image/jpeg;base64,{imgCV_base64}"
    # return f'{img_process.leftscore} vs {img_process.rightscore}'

if __name__ == "__main__":
    print('on hello')
    app.run(host="127.0.0.1", port=5000)