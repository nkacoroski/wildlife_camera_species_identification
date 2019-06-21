# functions for preprocessing data

import tensorflow as tf


def preprocess_image(image):
    """Take jpeg image, decode into tensor, resize, and normalize to [-1, 1] range"""
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [224, 224])
    image /= 255
    return image

def load_and_preprocess_image(path):
    """Take image from image path and decode into into tensor using preprocess function"""
    image = tf.io.read_file(path)
    return preprocess_image(image)