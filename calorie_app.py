import streamlit as st
from PIL import Image
import time
import random
import google.generativeai as genai

# Initialize Gemini API (Replace 'your-api-key' with an actual API key)
genai.configure(api_key="AIzaSyDcAD7rwUxJGfbnVVIoIhGmvIGrAE1xP2k")

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Calorie Counter", layout="wide")

st.title("🍔 Calorie Counter from Food Images")
st.write("Upload an image of your food, and we'll estimate the calories.")


uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])
st.subheader("🤖 Ask Gemini AI")
prompt = st.text_area("Enter your question:")
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
if st.button("Get Answer") and prompt:
    with st.spinner("Fetching response..."):
        response = get_gemini_response(prompt)
    st.write("### Gemini AI Response:")
    st.write(response)
