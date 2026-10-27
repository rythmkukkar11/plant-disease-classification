# Plant Disease Classification

A web app that identifies plant leaf diseases from a photo. Upload an image of a leaf and the app tells you the crop, the disease (or whether the leaf is healthy) and how confident the prediction is.

## About the Project
The model is built with transfer learning on MobileNetV2 and trained on the PlantVillage dataset, which covers 38 classes of healthy and diseased leaves across multiple crops. The trained model is served through a Streamlit web interface.

## Features
- Upload a leaf image (JPG, JPEG or PNG)
- Predicts one of 38 crop-disease classes
- Shows the prediction confidence in percent

## Tech Stack
- Python
- TensorFlow / Keras (MobileNetV2)
- Streamlit
- Pillow, NumPy

## Repository Files
| File | Description |
|------|-------------|
| `app.py` | Streamlit web app |
| `plant_model.keras` | Trained model |
| `class_names.json` | List of the 38 class labels |
| `requirements.txt` | Python dependencies |

## Run Locally
pip install -r requirements.txt
streamlit run app.py

## Team
- Rythm (Team Leader)
- Parv
- Keshav
- Lakshay

## Live Demo
Link will be added after deployment.
