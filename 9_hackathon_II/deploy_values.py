# In coder
# Run with `/home/your_name/.local/bin/streamlit  run deploy_transformer_streamlit.py`
# Check your port (usually 8501). Use the PORTS tab to forward the port to localhost

import streamlit as st
from transformers import pipeline

import pandas as pd
from autogluon.tabular import TabularPredictor
import os

# Dont use GPUS (they are usauall)
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# model_path = f"your path to the model"
# predictor = TabularPredictor.load(model_path)

def main():
    st.title("Use my cool ML model")
    st.write('Your inputs')
    # Create an inputs or sliders; up to you
    prop1 = st.slider('prop1', key='prop1', min_value=10, max_value=20)
    prop2 = st.text_input('prop2', key='prop2')
    prop3 = st.text_input('prop3', key='prop3')
    prop4 = st.text_input('prop4', key='prop4')
 

    # Create a button to trigger model inference
    if st.button("Predict"):
        st.subheader('This is the prediction')
        # Perform inference using the loaded model
        
        df = pd.DataFrame([[prop1, prop2, prop3, prop4]], columns=['prop1', 'prop2', 'prop3', 'prop4'])
        df
        # result = predictor.predict(df)
        # result


if __name__ == '__main__':
    main()
