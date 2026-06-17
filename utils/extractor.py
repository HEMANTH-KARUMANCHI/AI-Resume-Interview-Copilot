import re

SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "mysql", "postgresql",

    "machine learning", "ml", "deep learning", "nlp",
    "natural language processing", "computer vision",
    "data science", "data analysis", "predictive analytics",

    "pandas", "numpy", "matplotlib", "seaborn",
    "scikit-learn", "sklearn", "tensorflow", "keras",
    "pytorch", "opencv",

    "lightgbm", "gradient boosting", "xgboost",
    "pyspark", "pyspark ml", "spark", "databricks",

    "dask", "polars", "pydantic", "pandera",

    "openai", "openai api", "openai apis",
    "llm", "llms", "large language model",
    "generative ai", "genai", "transformers",
    "hugging face", "prompt engineering", "fine-tuning",
    "summarization",

    "shap", "lime", "xai", "explainable ai",
    "bleu", "rouge",

    "streamlit", "fastapi", "flask", "django",
    "api", "rest api",

    "git", "github", "docker", "aws", "azure", "gcp",

    "html", "css", "javascript", "react",

    "data preparation", "model deployment",
    "model monitoring", "data validation",
    "healthcare analytics"
]


def normalize_text(text):
    text=text.lower()
    text=text.replace("\n"," ")
    text=re.sub(r"[^a-z0-9+#.\s-]", " ", text)
    text=re.sub(r"\s+", " ", text)
    return text



def normalize_skill_names(skills):
    skill_map = {
        "Openai": "OpenAI",
        "Openai Api": "OpenAI API",
        "Openai Apis": "OpenAI API",
        "Llm": "LLM",
        "Llms": "LLM",
        "Ml": "Machine Learning",
        "Genai": "GenAI",
        "Generative Ai": "Generative AI",
        "Scikit-Learn": "Scikit-learn",
        "Sql": "SQL",
        "Api": "API",
        "Xai": "XAI",
        "Shap": "SHAP",
        "Lime": "LIME",
        "Bleu": "BLEU",
        "Rouge": "ROUGE",
    }

    normalized = []

    for skill in skills:
        normalized.append(skill_map.get(skill, skill))

    return sorted(set(normalized))


def extract_skills(text):
    if not text:
        return []
    
    text=normalize_text(text)
    found_skills=[]

    for skill in SKILL_KEYWORDS:
        skill_normalized=normalize_text(skill)

        if skill_normalized in text:
            found_skills.append(skill.title())

    return normalize_skill_names(sorted(set(found_skills)))

