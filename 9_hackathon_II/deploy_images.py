# In coder
# Run with `/home/your_name/.local/bin/streamlit  run deploy_transformer_streamlit.py`
# Check your port (usually 8501). 
# Use the PORTS tab in vscode to forward the port to localhost

import streamlit as st
from transformers import pipeline
import tempfile
import pandas as pd
from autogluon.multimodal import MultiModalPredictor
import os

# Dont use GPUS
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# model_path = f"your file"
# predictor = MultiModalPredictor.load(model_path)

def main():
    st.title("Use my cool ML model")
    # Create an input text box
    input_file = st.file_uploader('Upload your image file for analysis')

    # Create a button to trigger model inference
    if st.button("Predict area"):
        
        # Write the uploaded file to a temporary file (will be deleted automatically)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
            tmp.write(input_file.getvalue())
            # Show the uploaded figure (see API docs for the correct function)

            # Perform inference using the loaded model
            # result = predictor.predict(tmp.name)           
            # st.write(result)

if __name__ == '__main__':
    main()



