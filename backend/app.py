#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from pygrabber.dshow_graph import FilterGraph
import cv2
app = Flask(__name__)
cors = CORS(app)
graph = FilterGraph()
@app.route("/")
def hello():
    return 'test'

@app.route("/getvideoinput")
def get_video_devices():

    
    input_video_devices_list = graph.get_input_devices()

    print(input_video_devices_list)
    dic = {}
    for i, device in enumerate(input_video_devices_list):
        dic[device] = i

    return dic


if __name__ == "__main__":
    print('on hello')
    app.run(port=5000)