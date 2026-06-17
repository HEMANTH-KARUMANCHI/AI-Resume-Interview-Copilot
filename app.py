import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.extractor import extract_skills
from utils.matcher import calculated_match_score, get_matching_skills, get_missing_skills
from utils.llm_engine import analyze_resume_with_gemini

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
    jd_skills = extract_skills(job_description)\
    
    match_score= calculated_match_score(resume_skills, jd_skills)
    matching_skills=get_matching_skills(resume_skills, jd_skills)
    missing_skills=get_missing_skills(resume_skills, jd_skills)

    st.success("Resume and Job Description processed successfully!")
    st.subheader("Extracted Skills")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Resume Skills")
        st.write(", ".join(resume_skills) if resume_skills else "No skills found.")

    with col4:
        st.markdown("### Job Description Skills")
        st.write(", ".join(jd_skills) if jd_skills else "No skills found.")

    with st.expander("View extracted Resume text"):
        st.text_area(
            "Resume Content",
            resume_text,
            height=400
        )

    


    
    st.subheader("Match Analysis")

    st.metric("Resume Match Score", f"{match_score}%")

    col5, col6= st.columns(2)

    with col5:
        st.markdown('### Matching Skills')
        if matching_skills:
            st.success(", ".join(matching_skills))
        else:
            st.warning("No matching skills found.")

    with col6:
        st.markdown('### Missing Skills')
        if missing_skills:
            st.error(", ".join(missing_skills))
        else:
            st.success("No missing skills found. Great match!")


    
    st.subheader("AI Resume Analysis")

    if st.button("Generate AI Analysis"):
        with st.spinner("Analyzing Resume..."):

            analysis=analyze_resume_with_gemini(
                resume_text,
                job_description
            )

        st.markdown("---")
        st.markdown(analysis)
    