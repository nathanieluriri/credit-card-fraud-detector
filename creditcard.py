import streamlit as st

import pandas as pd
from joblib import load


st.set_page_config(page_title="Credit Card Anamaly",layout="wide")
st.title("Credit fraud detection")

st.file_uploader("Upload a csv containing the apporpriate information",type=["csv"],key="file")




# Load the model from a file
model = load('anomaly_detection_model.pkl')

if st.session_state.file:
    st.success("1= No fradulent activity detected -1 = Fradulent activity detected")
    col1,col2=st.columns([0.99,0.01])

    fr = pd.read_csv(st.session_state.file)
    try:
        fr = fr.drop("Class", axis=1)
        result=model.fit_predict(fr)
        with col1:
            st.write(fr)
        with col2:
            st.write(result)
    except:
        try:
            result=model.fit_predict(fr)
            st.write(fr)
            st.write(result)
        except:
            st.error("There is a problem with the dataset")
