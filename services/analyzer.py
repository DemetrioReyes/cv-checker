import re
from collections import Counter

def analyze_cv(text: str) -> dict:

    backend_skills_keywords = {
        "Python": 15, "Java": 12, "C#": 10, "Node.js": 10, "SQL": 10, "Django": 12, "Flask": 12, "AWS": 15, "Docker": 14, "Kubernetes": 14
    }

    frontend_skills_keywords = {
        "JavaScript": 12, "React": 15, "Vue.js": 14, "Angular": 14, "HTML": 10, "CSS": 10, "TypeScript": 12, "Redux": 13
    }

    general_skills_keywords = {
        "Git": 8, "CI/CD": 10, "Agile": 10, "Test Driven Development": 12, "Unit Testing": 10, "RESTful APIs": 14, "GraphQL": 13
    }

    education_keywords = ["Bachelor", "Master", "PhD", "Certification", "Bootcamp", "Licenciatura", "Maestría", "Doctorado", "Certificación", "Bootcamp"]
    experience_keywords = ["Junior", "Mid-level", "Senior", "Developer", "Engineer", "Software", "Junior", "Intermedio", "Senior", "Desarrollador", "Ingeniero", "Software"]
    
    ats_compliance = {
        "file_type": "pdf",
        "page_count": 2,
        "word_count": 500, 
        "phone_detected": r"\+?\d{10,15}",
        "email_detected": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA0-9]{2,}",
        "linkedin_detected": r"linkedin.com/in/",
        "education_section_detected": ["education", "educación"],
        "work_history_section_detected": ["work experience", "experiencia laboral"]
    }

    file_type_check = "pdf" if ".pdf" in text.lower() else "not pdf"
    page_count_check = len(re.findall(r"\f", text)) + 1
    word_count_check = len(text.split())
    phone_check = bool(re.search(ats_compliance["phone_detected"], text))
    email_check = bool(re.search(ats_compliance["email_detected"], text))
    linkedin_check = bool(re.search(ats_compliance["linkedin_detected"], text))
    education_section_check = any(degree.lower() in text.lower() for degree in education_keywords)
    work_history_section_check = any(section in text.lower() for section in ats_compliance["work_history_section_detected"])

    backend_skills_score = sum(value for key, value in backend_skills_keywords.items() if key.lower() in text.lower())
    frontend_skills_score = sum(value for key, value in frontend_skills_keywords.items() if key.lower() in text.lower())
    general_skills_score = sum(value for key, value in general_skills_keywords.items() if key.lower() in text.lower())

    experience_level = "Junior" if "Junior" in text or "Junior" in text else ("Mid-level" if "Mid-level" in text or "Intermedio" in text else ("Senior" if "Senior" in text or "Senior" in text else "Unknown"))

    pronouns_check = bool(re.search(r"\b(I|my|me|myself|yo|mi|me|mí)\b", text))
    numbered_data_check = bool(re.search(r"\d+", text))

    measurable_achievements_check = bool(re.search(r"\b(\d+%|\d+ years|achieved|increased|improved|años|logrado|incrementado|mejorado)\b", text))

    result = {
        "ATS_compliance": {
            "file_type": file_type_check,
            "page_count": page_count_check,
            "word_count": word_count_check,
            "phone_detected": phone_check,
            "email_detected": email_check,
            "linkedin_detected": linkedin_check,
            "education_section_detected": education_section_check,
            "work_history_section_detected": work_history_section_check
        },
        "skills_analysis": {
            "backend_skills_score": backend_skills_score,
            "frontend_skills_score": frontend_skills_score,
            "general_skills_score": general_skills_score,
            "backend_skills_found": [key for key in backend_skills_keywords if key.lower() in text.lower()],
            "frontend_skills_found": [key for key in frontend_skills_keywords if key.lower() in text.lower()],
            "general_skills_found": [key for key in general_skills_keywords if key.lower() in text.lower()]
        },
        "experience_level": experience_level,
        "lexical_analysis": {
            "pronouns_check": pronouns_check,
            "numbered_data_check": numbered_data_check
        },
        "semantic_analysis": {
            "measurable_achievements_check": measurable_achievements_check
        },
        "summary": {
            "total_score": backend_skills_score + frontend_skills_score + general_skills_score + (5 if experience_level != "Unknown" else 0)
        }
    }

    return result
