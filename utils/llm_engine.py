import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# For Streamlit Cloud deployment
if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)

def analyze_resume_with_gemini(resume_text, job_description):

    try:

        prompt = f"""
        Analyze the resume against the job description.

        Resume:
        {resume_text}

        Job Description:
        {job_description}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
⚠️ Gemini service is temporarily unavailable.

Error:
{str(e)}

Please try again after a few minutes.
"""