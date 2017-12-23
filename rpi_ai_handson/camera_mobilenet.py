from keras.applications.mobilenet import MobileNet
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input, decode_predictions
import numpy as np
import sys, os, time, subprocess, pickle

model = MobileNet(weights='imagenet')
devnull = open('os.devnull', 'w')

while True:
    subprocess.run(["wget", "-O", "photo.jpg", "http://192.168.1.46:8080/?action=snapshot"], stdout=devnull, stderr=subprocess.STDOUT)

    img_path = 'photo.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    print('Predicted:', decode_predictions(preds, top=3)[0])

# espeak
#    recognize = decode_predictions(preds)
#    speak = "This is a " + recognize[0][0][1]
#    subprocess.check_output(["espeak", "-k5", "-s150", speak])
#    print(speak)
