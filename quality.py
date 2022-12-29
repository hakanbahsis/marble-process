

from keras_preprocessing.image import load_img, img_to_array
import tensorflow as tf
import numpy as np


def MarbleQualityCheck(path):
    
    marbleModel = tf.keras.models.load_model('marble_quality_model.h5')
    img = tf.keras.utils.load_img(
        str(path), target_size=(180, 180)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = marbleModel.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_names = ['crack', 'dot', 'good', 'joint']

    
    return [ class_names[np.argmax(score)] , str( 100 * np.max(score) ),str(score)]
   