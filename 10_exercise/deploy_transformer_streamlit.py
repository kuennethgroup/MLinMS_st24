# Run with `pdm run streamlit run deploy_transformer_streamlit.py`


import streamlit as st
from transformers import pipeline

model = pipeline("sentiment-analysis")

def main():
    st.title("Sentiment analysis using transformers")

    st.text("The text will be analyzed regarding its sentiment.")
    # Create an input text box
    input_text = st.text_input("Enter your text", "")

    # Create a button to trigger model inference
    if st.button("Analyze"):
        # Perform inference using the loaded model
        result = model(input_text)
        for res in result:
            st.write("Prediction:", res['label'], "| Score:", res['score'])

if __name__ == '__main__':
    main()

