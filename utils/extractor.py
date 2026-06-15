import re

SKILL_KEYWORDS= [
    "Python", "C++", "Java", "JavaScript", "SQL", "HTML", "CSS", "React", "Node.js",
    "Django", "Flask", "Ruby", "PHP", "Swift", "Kotlin", "Rust", 
    "TypeScript", "Angular", "Machine Learning", "Deep Learning", "Data Science",
 "NLP", "Computer Vision", "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Pandas", "NumPy", 
 "Matplotlib", "Seaborn", "OpenCV", "Docker", "Kubernetes", "AWS", "Azure", "GCP",
    "Linux", "Git", "CI/CD", "Agile", "Scrum", "JIRA" ]


def extract_skills(text):
    text=text.lower()
    skills_found=[]

    for skill in SKILL_KEYWORDS:
        pattern= r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            skills_found.append(skill.title())

    return sorted(set(skills_found))