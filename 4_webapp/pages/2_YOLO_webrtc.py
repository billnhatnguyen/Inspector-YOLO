import streamlit as st 
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np
from yolo_predictions import YOLO_Pred  # make sure this is correctly implemented

st.set_page_config(page_title='Yolo Live Video',
                   layout='wide',
                   page_icon ='images/camera.png')

# Initialize YOLO model
try:
    yolo = YOLO_Pred('./models/best.onnx', './models/data.yaml')
except Exception as e:
    st.error(f"Error loading YOLO model: {e}")
    st.stop()

# Define callback
def video_frame_callback(frame):
    try:
        img = frame.to_ndarray(format="bgr24")
        pred_img = yolo.predictions(img)  # Ensure this returns a proper ndarray
        return av.VideoFrame.from_ndarray(pred_img, format="bgr24")
    except Exception as e:
        st.error(f"Error processing video frame: {e}")
        return av.VideoFrame.from_ndarray(img, format="bgr24")  # fallback

# Stream video
webrtc_streamer(
    key="example", 
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)
