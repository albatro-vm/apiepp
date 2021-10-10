from __future__ import division, print_function

# Flask 
from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename

import os
import numpy as np
import cv2
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from pandas.plotting import register_matplotlib_converters
from sklearn.model_selection import train_test_split
import urllib
import time
from PIL import Image
import skimage.io as io
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color

# Cargamos el modelo
from keras.models import load_model
from keras_retinanet import models


# Cargamos el archivo que contiene las etiquetas de las clases
labels_to_names = pd.read_csv('classes.csv', header=None).T.loc[0].to_dict()

# Definimos una instancia de Flask
app = Flask(__name__)

#app=Flask(__name__,template_folder='templates')

model_path = os.path.join('snapshots', sorted(os.listdir('snapshots'), reverse=True)[0])
model = models.load_model(model_path, backbone_name='resnet50')
model = models.convert_model(model)
print('Modelo cargado exitosamente. Verificar http://127.0.0.1:5000/')


##############################################
def predict(image):
  image = preprocess_image(image.copy())
  image, scale = resize_image(image)
 
  boxes, scores, labels = model.predict_on_batch(
    np.expand_dims(image, axis=0)
  )
  boxes /= scale

  return boxes, scores, labels

##############################################
umbralScore = 0.5
epps = []

def getEpps(scores, labels):
    for score, label in zip(scores[0], labels[0]):
        if score < umbralScore:
            break
        epps.append({'epp':labels_to_names[label],'value':float(score)})
     
@app.route('/predict/<string:img_path>')
def getPredicResult(img_path):
    img_name = img_path
    image = io.imread(img_path) 
    boxes, scores, labels = predict(image)  
    getEpps(scores, labels)
    return jsonify({img_name: epps})

if __name__ == '__main__':   
    app.run()
