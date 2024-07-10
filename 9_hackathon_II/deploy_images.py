# In coder
# Run with `pdm run streamlit run 9_hackathon_II/deploy_images.py`
# Check your port (usually 8501). 
# Use the "PORTS" tab in VScode to forward the port to localhost and view it your local browser
# OR use preview browser in VScode

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



