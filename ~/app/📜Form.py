import streamlit as st
import pandas as pd
from deta import Deta
import json
import base64
from PIL import Image

image = Image.open('image_1.png')

col1, col2 = st.columns(2)

col1.header("Pink Data Hub CRM")
col2.image(image)

pink_data = st.sidebar.selectbox("choose:",("Chose","Database", "Database Connection"))


deta = Deta(st.secrets["deta_key"])

db = deta.Base("CRM-Records")
 
          
if pink_data == "Database":
          with st.form("Submit", clear_on_submit=True):
               id_name = st.text_input("Company's ID")
               name = st.text_input("Company's Name")
               phone = st.text_input("Company's Phone Number")
               email = st.text_input("Company's Email Address")
               location = st.text_input("Company's Location")
               submitted = st.form_submit_button("Submit")
               if submitted:
                     db.put({"company_id":id_name, "company_name":name, "email_address":email, "location":location})
