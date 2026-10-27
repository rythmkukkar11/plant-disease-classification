import streamlit as st, tensorflow as tf, json, numpy as np
from PIL import Image

@st.cache_resource
def load():
    return tf.keras.models.load_model("plant_model.keras")

model = load()
names = json.load(open("class_names.json"))
st.title("Plant Disease Detection")
f = st.file_uploader("Leaf image upload karo", type=["jpg", "jpeg", "png"])
if f:
    img = Image.open(f).convert("RGB").resize((128, 128))
    st.image(img)
    x = np.expand_dims(np.array(img).astype("float32"), 0)
    p = model.predict(x)[0]
    st.success(f"{names[p.argmax()]} ({p.max()*100:.1f}%)")
