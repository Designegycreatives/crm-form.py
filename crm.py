import streamlit as st
import datetime
import pandas as pd



st.header("Pink Data Hub CRM")

pink_data = st.sidebar.selectbox("Database", "Database Connection")


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

"---"


if pink_data ==  'Database Connection':
    db_content = db.fetch().items
    st.write(db_content)
