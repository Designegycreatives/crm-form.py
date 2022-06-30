import streamlit as st
import pandas as pd
from deta import Deta
import json
import base64
from PIL import Image

image = Image.open('image1.png')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.header("Pink Data Hub CRM")

col1.write("A form app with DETA.SH Database")

col2.image(image)

col1.image(image1)


deta = Deta(st.secrets["deta_key"])

db = deta.Base("CRM-Records")
 
          

with st.form("Submit", clear_on_submit=True):
     id_name = col3.text_input("Company's ID")
     name = col4.text_input("Company's Name")
     phone = col3.text_input("Company's Phone Number")
     email = col4.text_input("Company's Email Address")
     location = col3.text_input("Company's Location")
     submitted = st.form_submit_button("Submit")
     if submitted:
        st.write("Submitted Successfully")
        db.put({"company_id":id_name, "company_name":name, "email_address":email, "location":location})
