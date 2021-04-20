import cv2
import numpy as np
import streamlit as st
from PIL import Image
import os
from utiles import read_file


def image_info():

    st.header("= Information on the image =")
    st.write("------------------------------")

    image_file = st.file_uploader(
        "Upload image : ", type=['jpg', 'png', 'jpg'])
    if image_file is not None:
        file_details = {"File Name": image_file.name,
                        "File Type": image_file.type}

        # @ save image
        with open(os.path.join("uploaded_image", image_file.name), "wb") as f:
            f.write(image_file.getbuffer())

        img_file = "uploaded_image/" + file_details['File Name']
        img = read_file(img_file)

    file_details30 = {"File Name": image_file.name,
                      "File Type": image_file.type, "Height": img.shape[0], "Width": img.shape[1], "channels": img.shape[2]}

    st.write(file_details30)
    st.image(image_file, use_column_width=True)
