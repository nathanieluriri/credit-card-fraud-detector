import streamlit as st

import pandas as pd
from joblib import load













if "model" not in st.session_state:
    st.session_state.model=load('anomaly_detection_model.pkl')


if "prediction" not in st.session_state:
    st.session_state.prediction=None


st.set_page_config(page_title="Credit Card Anamaly",layout="wide",initial_sidebar_state="expanded")
st.title("Credit fraud detection")
st.info("1= No fradulent activity detected -1 = Fradulent activity detected")








import pandas as pd

import pandas as pd

def create_dataframe():
    data = {
        'Time': [st.session_state.time],
        'V1': [st.session_state.v1],
        'V2': [st.session_state.v2],
        'V3': [st.session_state.v3],
        'V4': [st.session_state.v4],
        'V5': [st.session_state.v5],
        'V6': [st.session_state.v6],
        'V7': [st.session_state.v7],
        'V8': [st.session_state.v8],
        'V9': [st.session_state.v9],
        'V10': [st.session_state.v10],
        'V11': [st.session_state.v11],
        'V12': [st.session_state.v12],
        'V13': [st.session_state.v13],
        'V14': [st.session_state.v14],
        'V15': [st.session_state.v15],
        'V16': [st.session_state.v16],
        'V17': [st.session_state.v17],
        'V18': [st.session_state.v18],
        'V19': [st.session_state.v19],
        'V20': [st.session_state.v20],
        'V21': [st.session_state.v21],
        'V22': [st.session_state.v22],
        'V23': [st.session_state.v23],
        'V24': [st.session_state.v24],
        'V25': [st.session_state.v25],
        'V26': [st.session_state.v26],
        'V27': [st.session_state.v27],
        'V28': [st.session_state.v28],
        'Amount': [st.session_state.amount],
    }
    df = pd.DataFrame(data)
    return df



def create_result_dataframe():
    # Get the prediction dataframe from the session state
    prediction_df = st.session_state.prediction

    # Perform model fitting and prediction
    result_from_users = st.session_state.model.fit_predict(prediction_df)

    # Create a new DataFrame with the prediction results
    result_df = pd.DataFrame({'Prediction Results': result_from_users})

    # Add the original prediction dataframe as a new column
    combined_df = pd.concat([prediction_df,result_df], axis=1)

    return combined_df







st.file_uploader("Upload a csv containing the apporpriate information",type=["csv"],key="file")
one,two= st.tabs([" **:gray[**User Uploaded File**]** &mdash; :sunflower::blossom: ","**:gray[**User filled in the details manually**]** &mdash;  :rose::hibiscus:"])
with st.sidebar:
    st.number_input("Enter Details For time",key="time",step=1,min_value=0)
    for i in range(1, 29):
        st.number_input(f"Enter details for v{i}", key=f"v{i}")
    st.number_input("Enter Details For Amount ",key="amount")

# Load the model from a file

with one:
    if st.session_state.file:

        col1,col2=st.columns([0.99,0.01])

        fr = pd.read_csv(st.session_state.file)
        try:
            fr = fr.drop("Class", axis=1)
            result=st.session_state.model.fit_predict(fr)
            with col1:
                st.write(fr)
            with col2:
                st.write(result)
        except:
            try:
                result=st.session_state.model.fit_predict(fr)
                st.write(fr)
                st.write(result)
            except:
                st.error("There is a problem with the dataset you uploaded")


with two:
    st.session_state.prediction=create_dataframe()
    
    if st.button("**:gray[**make prediction**]**",type="primary"):
        st.success("Predicted result column is the last one so keep on scrolling")
        result_from_users=st.session_state.model.fit_predict(st.session_state.prediction)
        st.write(create_result_dataframe())
        st.snow()








