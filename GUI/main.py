import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000)

st.title("PP ")
st.header("雞舍 :blue[溫度]& :red[光線]")
st.divider()



url = 'https://blynk.cloud/external/api/get?token=   &v0&v1'

response = requests.request("GET",url)
if response.status_code == 200:
    all_data = response.json()
    st.info(f'光線:{all_data["v0"]}')
    st.warning(f'可變電阻:{all_data["v1"]}')
else:
    st.write("連線失敗,請等一下再試")