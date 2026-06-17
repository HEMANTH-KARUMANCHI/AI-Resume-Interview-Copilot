RESUME_ANALYSIS_PROMPT="""

You are an expert AI recruiter.

Analyze the candidate's resume and compare it with the job description.

Provide:
1. Overall Resume Match Summary
2. Candidate Strengths
3. Weak Areas / Gaps
4. Missing Skills
5. Resume Improvements Suggestions
6. Learning Recommendations
7. Interview Preparation Topics


Resume:
{resume_text}

Job Description:
{job_description}
"""