# 🤖 AI Resume & Interview Copilot

An AI-powered application that analyzes a candidate's resume against a job description to provide intelligent career insights, including skill extraction, job matching, skill-gap analysis, personalized recommendations, and interview preparation support.

## 📌 Project Objective

Job seekers often struggle to understand how well their resume matches a job description and what skills they need to improve. This project aims to bridge that gap using NLP and Large Language Models (LLMs).

The goal is to build a practical AI application that demonstrates real-world GenAI engineering skills beyond a simple chatbot.

---

## 🚀 Features Implemented

### ✅ Phase 1: Project Setup

* Professional Python project structure
* Virtual environment setup
* Git and GitHub integration
* `.gitignore` configuration
* Streamlit application setup

### ✅ Phase 2: Resume Processing

* Upload resumes in PDF format
* Extract text from multi-page PDF resumes using `pdfplumber`
* Display extracted resume content within the application

### ✅ Phase 3: Skill Extraction

* Accept job descriptions as text input
* Extract skills from resumes
* Extract skills from job descriptions
* Display resume skills and job description skills side-by-side

---

## 🏗️ Project Architecture

```text
User Uploads Resume (PDF)
            ↓
      Resume Parser
            ↓
     Skill Extraction
            ↓
   Job Description Input
            ↓
 Job Description Analysis
            ↓
 Display Extracted Skills
```

---

## 📂 Project Structure

```text
AI_Resume_Matcher/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env
│
├── assets/
│
├── core/
│   └── pipeline.py
│
├── data/
│
├── utils/
│   ├── parser.py
│   ├── extractor.py
│   ├── matcher.py
│   ├── llm_engine.py
│   └── prompts.py
│
└── venv/
```

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Libraries

* pdfplumber
* pandas
* regex
* python-dotenv
* OpenAI API (planned)

### Version Control

* Git
* GitHub

### Deployment

* Streamlit Cloud (planned)

---

## 📸 Current Workflow

1. Upload a PDF resume.
2. Extract resume text.
3. Paste a job description.
4. Extract skills from the resume.
5. Extract skills from the job description.
6. Display both skill sets for comparison.

---

## 🔜 Upcoming Features

### Phase 4: Matching Engine

* Match percentage calculation
* Matching skills identification
* Missing skills detection

### Phase 5: AI Enhancements

* Resume improvement suggestions
* Skill-gap analysis using LLMs
* Personalized learning recommendations

### Phase 6: Interview Preparation

* Technical interview questions
* Behavioral interview questions
* Role-specific interview preparation

### Phase 7: Advanced Features

* ATS score estimation
* Resume section analysis
* PDF report export
* Multiple job description comparison
* Streamlit Cloud deployment

---

## 🎯 Key AI Concepts Demonstrated

* Resume Parsing
* Information Extraction
* Natural Language Processing (NLP)
* Skill Extraction
* Recommendation Systems
* Prompt Engineering (planned)
* Large Language Model Integration (planned)
* AI-Assisted Career Guidance

---

## 👨‍💻 Author

**Hemanth Karumanchi**

Built as a practical GenAI project to strengthen applications for AI Engineer, GenAI Engineer, Machine Learning Engineer, Data Science, and Software Engineering roles.