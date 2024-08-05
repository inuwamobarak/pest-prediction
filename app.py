import streamlit as st
from fastai.vision.all import load_learner
from PIL import Image
import io
import base64

# Load the trained model
learn = load_learner('model/pest_model.pkl')


def predict(image):
    # Resize the image (replace 128 with the size used during training)
    img = image.resize((128, 128))

    # Get the model prediction
    pred_class, pred_idx, probabilities = learn.predict(img)

    # Convert tensor probabilities to a list of rounded values
    probabilities = [round(float(prob), 4) for prob in probabilities]

    # Return the prediction result
    return pred_class, pred_idx, probabilities


def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# Background image
set_background('images/bg2.jpg')

st.title("Pest Image Classifier")

# Custom styles
st.markdown(
    """
    <style>
    .title {
        font-family: 'Arial';
        color: white;
        text-align: center;
    }
    .radio {
        color: white;
        font-size: 18px;
    }
    .upload {
        color: white;
        font-size: 16px;
    }
    .result {
        font-size: 20px;
        color: yellow;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Upload an image or use the camera
option = st.radio("Choose an option", ("Upload an image", "Use camera"))

if option == "Upload an image":
    uploaded_file = st.file_uploader("Upload an image of the pest", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        pred_class, pred_idx, probabilities = predict(image)
        threshold = 0.5  # Set your threshold here
        if max(probabilities) < threshold:
            st.markdown(f"<div class='result'>No pest detected.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result'>Predicted Class: {pred_class}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result'>Probabilities: {probabilities}</div>", unsafe_allow_html=True)

elif option == "Use camera":
    picture = st.camera_input("Take a picture of the pest")
    if picture:
        image = Image.open(picture)
        st.image(image, caption='Captured Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        pred_class, pred_idx, probabilities = predict(image)
        threshold = 0.5  # Set your threshold here
        if max(probabilities) < threshold:
            st.markdown(f"<div class='result'>No pest detected.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result'>Predicted Class: {pred_class}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result'>Probabilities: {probabilities}</div>", unsafe_allow_html=True)

st.markdown("<hr><center><a href='https://pngtree.com/freebackground/agricultural-technology-green-field"
            "-background_1473313.html'>free background photos from pngtree.com</a></center>", unsafe_allow_html=True)
