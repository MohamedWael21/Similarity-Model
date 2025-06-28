from keras.applications import EfficientNetB0
from keras.utils import load_img, img_to_array
from keras.layers import Rescaling, GlobalAveragePooling2D
from keras.models import Sequential
import numpy as np

class SimilarityModel:
    def __init__(self):
        self.model = None
    
    def get_model(self):
        """Get the similarity model (EfficientNetB0 feature extractor)"""
        if self.model is None:
            base_model = EfficientNetB0(weights='imagenet', include_top=False)
            base_model.trainable = False
            self.model = Sequential([
                Rescaling(1./255),
                base_model,
                GlobalAveragePooling2D()
            ])
        return self.model
    
    def get_image_vector(self, image_path):
        """Convert image to vector format for model input"""
        img = load_img(image_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) 
        return img_array
