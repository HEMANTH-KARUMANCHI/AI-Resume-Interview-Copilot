import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.extractor import extract_skills

st.set_page_config(
    page_title="🤖 AI Resume & Interview Copilot 🤖",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume & Interview Copilot 🤖")

st.write("Upload your resume and compare it with a job description.")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "Paste Job Description Here:",
        height=250,
        placeholder="Paste the job description here.."
    )

if uploaded_file is not None and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    st.success("Resume and Job Description processed successfully!")
    st.subheader("Extracted Skills")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Resume Skills")
        st.write(resume_skills)

    with col4:
        st.markdown("### Job Description Skills")
        st.write(jd_skills)

    with st.expander("View extracted Resume text"):
        st.text_area(
            "Resume Content",
            resume_text,
            height=400
        )