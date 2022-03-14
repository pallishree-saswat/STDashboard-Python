import streamlit as st
import pandas as pd
import numpy as np

# st.title('Uber pickups in NYC')
# dataframe = np.random.randn(10,20)
# st.dataframe(dataframe)

uploaded_file = st.file_uploader("upload files", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # df = df[df['OPEN_INT'] > 0]
    # df['TIMESTAMP']=pd.to_datetime(df["TIMESTAMP"])
    st.dataframe(df)

    # metadata = df
    # option = st.sidebar.selectbox('Symbol', metadata['SYMBOL'].unique())

