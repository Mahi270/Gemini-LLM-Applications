from dotenv import load_dotenv # type: ignore
load_dotenv() #loading all the env vars

import streamlit as st  # type: ignore
import os

import google.generativeai as genai # type: ignore

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get reponses

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#initializing the streamlit app (for frontend purposes)
st.set_page_config(page_title = "Q&A Demo")

st.header("ChatWizard - A Gemini LLM Powered Application")

input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

## When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is: ")
    st.write(response)