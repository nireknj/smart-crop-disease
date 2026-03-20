import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions

# Load a pre-trained Keras model globally (ImageNet mode for Phase 1 stub)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

REMEDY_MAP = {
    # To be populated when training on plant disease datasets
}

def predict_disease(tensor) -> dict:
    preds = model.predict(tensor)
    top_pred = decode_predictions(preds, top=1)[0][0]
    class_id, name, score = top_pred
    
    remedy = REMEDY_MAP.get(name, "Maintain moderate watering passing standard fungicide if symptoms persist.")
    return {
        "disease": name,
        "confidence": float(score),
        "remedy": remedy
    }
