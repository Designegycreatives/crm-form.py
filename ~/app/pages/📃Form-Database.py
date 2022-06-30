import streamlit as st
import pandas as pd
from deta import Deta
import json
import base64
from PIL import Image

image = Image.open('image_1.png')

col1, col2 = st.columns(2)

col1.header("Pink Data Hub CRM Database")
col2.image(image)


deta = Deta(st.secrets["deta_key"])

db = deta.Base("CRM-Records")

db_content = db.fetch().items
st.write(db_content)



