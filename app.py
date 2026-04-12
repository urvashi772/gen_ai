import streamlit as st
import PyPDF2
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

# Gemini API setup
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function: Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    
    return text

# Function: Generate questions using Gemini
def generate_questions(profile_text):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are an interviewer.

    Based on the candidate profile below, generate 5 behavioral interview questions.

    Candidate Profile:
    {profile_text}
    """

    response = model.generate_content(prompt)
    return response.text


# Streamlit UI
st.title("🎤 AI Interview Bot")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    # Extract text
    profile_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Profile")
    st.write(profile_text[:1000])  # preview

    if st.button("Generate Interview Questions"):
        questions = generate_questions(profile_text)

        st.subheader("💡 Interview Questions")
        st.write(questions)