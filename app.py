import streamlit as st
import numpy as np
from PIL import Image
from utils import set_background
import requests

set_background("./imgs/background.png")

header = st.container()
body = st.container()

def model_prediction(img):
    """
    temp_img_path = f"./temDir/{img.name}"
    with open(temp_img_path,"wb") as f:
        f.write(img.getbuffer())    
    resp = requests.post("http://127.0.0.1:5000", files={'file': open(temp_img_path, 'rb')})
    """

    bytes_data = img.getvalue()

    resp = requests.post("http://3.142.149.97:5000/", files={'file': bytes_data})

    return resp.json()
    
with header :
    _, col1, _ = st.columns([0.15,1,0.1])
    col1.title("Testing AWS EC2 Virtual Machine Server 🔎")

with body :
    img = st.file_uploader("Upload an Image:", type=["png", "jpg", "jpeg"])

    _, col2, _ = st.columns([0.3,1,0.2])

    _, col5, _ = st.columns([0.8,1,0.2])
    
    if img is not None:
        image = np.array(Image.open(img))    
        col2.image(image, width=400)

        if col5.button("Predict"):
            result = model_prediction(img)

            _, col3, _ = st.columns([0.7,1,0.2])
            col3.header("Results ✅:")

            _, col4, _ = st.columns([0.4,1,0.4])
            col4.success(result)

            
