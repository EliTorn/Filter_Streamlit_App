from io import BytesIO
import streamlit as st
from PIL import Image
from filter import Filter


def download_image():
    # Convert PIL Image to bytes
    modified_image_bytes = BytesIO()
    modified_image.save(modified_image_bytes, format="JPEG")  # Change format as needed

    # Use st.download_button from the st object
    st.download_button(label="Download image",
                       data=modified_image_bytes.getvalue(),
                       file_name="modified.jpeg",
                       mime="image/jpeg")


# Page title
st.title("Image Uploader")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    f = Filter(image, image.width, image.height)
    modified_image = f.buttons()
    col1, col2 = st.columns(2)
    col1.image(image, caption='Uploaded Image')

    if modified_image is not None:
        col2.image(modified_image, caption='Modified Image')
        download_image()

else:
    st.warning("Please upload an image.")
