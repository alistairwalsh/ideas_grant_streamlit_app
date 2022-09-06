
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import pandas as pd
import numpy as np
import requests
from io import StringIO

# https://education.arcus.chop.edu/redcap-api/

st.title("hello")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

# df = pd.read_csv(StringIO(r.text))
# df

#picture = st.camera_input("Take a picture")

#if picture:
#     st.image(picture)

#data = {
#    'token': 'C0ADB9762F115D7200E32784AAE3E3D0',
#    'content': 'metadata',
#    'format': 'json',
#    'returnFormat': 'json'
#}
#r = requests.post('https://redcap.latrobe.edu.au/redcap/api/',data=data)
#st.write('HTTP Status: ' + str(r.status_code))
#st.write(r.json())
#st.write(data)
