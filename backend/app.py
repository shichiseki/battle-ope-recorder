#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from concurrent.futures import thread
import time
from queue import Queue
from flask import Flask, render_template, jsonify, request, Response
from flask_cors import CORS
from pygrabber.dshow_graph import FilterGraph
import cv2
import functools
app = Flask(__name__)
cors = CORS(app)
graph = FilterGraph()

singleQueue = Queue(maxsize=1)

# class LifeGameCamera():
#     def __init__(self):
#         self.video_id = None
    
#     def draw_image(self):
#         self.video_capture = cv2.VideoCapture(self.video_id, cv2.CAP_DSHOW)
#         ret, frame = self.video_capture.read()
#         return frame
        
#     def get_frame(self):
#         image = self.draw_image()  # OpenCVを使って描画
#         _, encimg = cv2.imencode('.png', image)
#         return encimg.tobytes()

class CameraInfo:
    def __init__(self):
        self.video_id = None
        self.current_id = None
        self.flag = True
        self.video_capture = [None] * 5
        self.kill_list = {}
        self.camids = {}


def multiple_control(q):
    def _multiple_control(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            q.put(time.time())
            print("/// [start] critial zone")
            result = func(*args,**kwargs)
            print("/// [end] critial zone")
            q.get()
            q.task_done()
            return result

        return wrapper
    return _multiple_control

camera_info = CameraInfo()

def gen(id):
    cam = cv2.VideoCapture(id, cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    # cam.set(cv2.CAP_PROP_FPS, 60)
    # cam.release()
    # cam = camera_info.video_capture[id].
    camera_info.camids[id] = 'exist'
    print('genin')
    while True:
        ret, frame = cam.read()
        # time.sleep(0.4)
        print(id, ret, cam.isOpened())
        

        if not cam.isOpened():
            cam.release()
            cam = cv2.VideoCapture(id, cv2.CAP_DSHOW)

        if ret:
            frame = cv2.resize(frame, dsize=(640, 360))
            _, encimg = cv2.imencode('.jpg', frame)
            print(frame.shape)
            frame = encimg.tobytes()
            # print('st')
            yield b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
        
        if id != camera_info.video_id:
            print('out!', id)
            yield 1
            # cam.release()
            exit()

@app.route("/")
def hello():

    return 'test'

@app.route("/getvideoinput")
def get_video_devices():

    input_video_devices_list = graph.get_input_devices()

    print(input_video_devices_list)
    dic = {'devices':[]}
    for i, device_name in enumerate(input_video_devices_list):
        device_dic = {}
        device_dic['id'] = i
        device_dic['name'] = device_name
        dic['devices'].append(device_dic)

    return dic


@app.route("/post_video_id", methods=["POST"])
def video_frame():
    # camera_info.video_id = int(request.get_json()['video_id'])
    camera_info.flag = False
    # return Response(gen(camera_info.video_id), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return Response(gen(camera_info.video_id), mimetype='multipart/x-mixed-replace; boundary=frame')
    return 'test'


@app.route('/video/<int:id>/',  methods=["GET"])
def video(id):
    camera_info.video_id = id
    print('get video', id)
    return Response(gen(id), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    print('on hello')
    app.run(host="127.0.0.1", port=5000, threaded=True)