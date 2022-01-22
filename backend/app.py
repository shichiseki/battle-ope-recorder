#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    return 'test'

if __name__ == "__main__":
    print('on hello')
    app.run(port=5000)