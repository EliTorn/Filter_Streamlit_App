import streamlit as st
from PIL import Image
from filter import Filter

# Page title
st.title("Image Uploader")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if an image is uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    f = Filter(image, image.width, image.height)
    modified_image = f.buttons()
    col1, col2 = st.columns(2)
    col1.image(image, caption='Uploaded Image')

    if modified_image is not None:
        col2.image(modified_image, caption='Modified Image')

else:
    st.warning("Please upload an image.")
