from dotenv import load_dotenv # type: ignore
load_dotenv() #loading all the env vars

import streamlit as st  # type: ignore
import os

import google.generativeai as genai # type: ignore
from PIL import Image # type: ignore

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro vision model and get reponses

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

##initialize the streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("ChatImage - A Gemini powered Application")
input = st.text_input("Input Prompt: ",key = "input")

#for uploading an image file

uploaded_file = st.file_uploader("Choose an image...", type = ["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Tell me about the image")

##if submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is: ")
    st.write(response)