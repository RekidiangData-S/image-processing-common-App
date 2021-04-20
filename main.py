import streamlit as st
from PIL import Image
import cv2
import numpy as np
# import inner module
from image_info import image_info
from algebra_operation import algebra_operation
from logical_operation import logical_operation
from geometric_operation import geometric_operation
from image_transformation import image_transformation
from image_enhancement import image_enhancement
from image_restoration import image_restoration
from image_compression import image_compression
from image_segmentation import image_segmentation
from color_image_processing import color_image_processing
from image_representation_and_description import image_representation_and_description
from about import about
#from login import connexion


def mains():
    st.header('Image Processing with OpenCv')
    st.image('logo_resized.png', use_column_width=True)

    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Image Information', 'Algebra operation', 'Logical Operation', 'Geometric Operation',
         'Image Transformation', 'Image Enhancement', 'Image Restoration', 'Image Compression',
         'Image Segmentation', 'Color Image Processing', 'Image Representation and Description', 'About'
         )
    )

    if selected_box == 'Image Information':
        image_info()
    if selected_box == 'Algebra operation':
        algebra_operation()

    if selected_box == 'Logical Operation':
        logical_operation()
    if selected_box == 'Geometric Operation':
        geometric_operation()
    if selected_box == 'Image Transformation':
        image_transformation()
    if selected_box == 'Image Enhancement':
        image_enhancement()
    if selected_box == 'Image Restoration':
        image_restoration()
    if selected_box == 'Image Compression':
        image_compression()
    if selected_box == 'Image Segmentation':
        image_segmentation()
    if selected_box == ' Color Image Processing':
        color_image_processing()
    if selected_box == 'Image Representation and Description':
        image_representation_and_description()
    if selected_box == 'About':
        about()


if __name__ == "__main__":
    mains()
