import streamlit as st
import pandas as pd
from io import StringIO
import numpy as np
import json

st.title(":zap:Telegram Dashboard")
with st.expander("Statistics"):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

#         data = json.loads(string_data)
#         st.json(data)
