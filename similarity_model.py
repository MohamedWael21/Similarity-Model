from keras.applications import EfficientNetB0
from keras.utils import load_img, img_to_array
from keras.layers import Rescaling, GlobalAveragePooling2D
from keras.models import Sequential
import numpy as np

def get_similarity_model():
    base_model = EfficientNetB0(weights='imagenet', include_top=False)
    base_model.trainable = False
    feature_extractor = Sequential([
    Rescaling(1./255),
    base_model,
    GlobalAveragePooling2D()
])
    return feature_extractor

def get_image_vector(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) 
    return img_array
