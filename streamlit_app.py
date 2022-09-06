
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import pandas as pd
import numpy as np
import requests
from io import StringIO

# https://education.arcus.chop.edu/redcap-api/

st.title("hello")

webrtc_streamer(key="sample")

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
