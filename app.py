import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the pre-trained model
model = load_model('models\cnn_model.h5')

# Define a function to preprocess the uploaded image
def preprocess_image(img):
    img = img.resize((128, 128))  # Resize to match the input shape of the model
    img = img.convert('L')  # Convert to grayscale if necessary
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize to [0,1]
    return img_array

# Streamlit app
st.title("Parkinson's Disease Prediction from Spiral Drawings")

st.write("Upload a hand-drawn spiral image to predict the likelihood of Parkinson's disease.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    # Layout: Image on left, prediction result on right
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(img, caption='Uploaded Image', width=225)

    # Preprocess image & make prediction
    img_array = preprocess_image(img)
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)

    with col2:
        st.write("### Prediction Result")
        if predicted_class[0] == 0:
            st.success("**Healthy**")
        else:
            st.error("**Parkinson's Disease Detected**")