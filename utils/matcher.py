"""
calculate the match percentage based on jd skills covered by resume
"""
def calculated_match_score(resume_skills, jd_skills):

    if not jd_skills:
        return 0
    
    resume_set=set(resume_skills)
    jd_set=set(jd_skills)

    matched_skills=resume_set.intersection(jd_set)
    score=(len(matched_skills)/len(jd_skills))*100

    return round(score, 2)


"""
Get the list of matching skills between resume and job description
"""
def get_matching_skills(resume_skills, jd_skills):
    return sorted(set(resume_skills).intersection(set(jd_skills)))

"""
Get the list of missing skills that are in the job description but not in the resume
"""
def get_missing_skills(resume_skills, jd_skills):
    return sorted(set(jd_skills).difference(set(resume_skills)))
