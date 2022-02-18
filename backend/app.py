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

    img_process.image_process(imgCV)
    
    return f'{img_process.leftscore} vs {img_process.rightscore}'

if __name__ == "__main__":
    print('on hello')
    app.run(host="127.0.0.1", port=5000)