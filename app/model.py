# -*- coding: UTF-8 -*-
import numpy as np
import tensorflow as tf
import cv2


model_load = tf.keras.models.load_model('app/best_img_model')
img_height = 180
img_width = 180

def imagepredict(frame): 
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) 
    predictions = model_load.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    class_names = ['00','01','02','03','04','05','06','07','08','09']
    predic_class = class_names[np.argmax(score)]
    return predic_class,100 * np.max(score)

    
