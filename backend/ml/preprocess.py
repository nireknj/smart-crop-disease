import io
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def process_image(file_bytes: bytes) -> np.ndarray:
    image = Image.open(io.BytesIO(file_bytes))
    image = image.convert("RGB")
    image = image.resize((224, 224))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)
