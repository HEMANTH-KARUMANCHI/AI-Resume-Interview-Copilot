import os
from dotenv import load_dotenv
from google import genai
from utils.prompts import RESUME_ANALYSIS_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume_with_gemini(resume_text, job_description):

    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text