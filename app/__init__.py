# -*- coding: UTF-8 -*-
import numpy as np
from flask import Flask,request,jsonify
from flask_cors import CORS
from os import listdir
from os.path import isfile, isdir, join
import tensorflow as tf
import cv2
import app.model as model

app = Flask(__name__)
CORS(app)


@app.route('/predict',methods=['post'])
def getInput():
    f = request.files['file']
    classname = request.args.get('classname')
    img = f.read()
    im1 = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
    predic_class , score = model.imagepredict(im1)
    print(predic_class , score,classname)
    if score<70:
        predic_class='00'
    if str(predic_class)==classname:
        re = 'False'
    else:
        re = 'True'
    return re



    
