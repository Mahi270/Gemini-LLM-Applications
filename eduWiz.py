from dotenv import load_dotenv # type: ignore
load_dotenv() #loading all the env vars

import streamlit as st  # type: ignore
import os
import google.generativeai as genai # type: ignore

# Configure the Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response #the output

# Initializing the Streamlit app (for frontend purposes)
st.set_page_config(page_title="Educational AI Assistant")

st.header("EduWizard - Your Personal Educational Assistant")

#Initialize session state for chat history if it doesn't already exist

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Prompt the user to enter their educational query
input = st.text_input("Ask a question about any educational topic: ", key="input")
submit = st.button("Get Answer")

# When submit is clicked
if submit and input:
    response = get_gemini_response(input)
    
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is:")
    
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is: ")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    
# Additional educational features
st.sidebar.header("EduWizard Features")
st.sidebar.write("""
- **Subject-specific Assistance**: Ask questions related to various subjects such as Math, Science, History, and more.
- **Homework Help**: Get help with your homework problems.
- **Concept Explanations**: Ask for detailed explanations of complex concepts.
- **Resource Suggestions**: Get recommendations for further reading and study materials.
""")

# Example questions for users to try
st.sidebar.subheader("Example Questions")
st.sidebar.write("""
- "Can you explain the Pythagorean theorem?"
- "What are the causes of the French Revolution?"
- "How does photosynthesis work?"
- "What is the capital of France?"
""")
