from typing import Dict, List, Tuple
import re

class JobMatcher:
    def __init__(self):
        self.required_skills = {
            "python": {"weight": 15, "alternatives": ["python"]},
            "django": {"weight": 8, "alternatives": ["django", "flask", "fastapi"]},  # Frameworks equivalentes
            "database": {"weight": 10, "alternatives": ["mysql", "postgresql", "oracle", "sql", "sqlite"]},
            "web_development": {"weight": 8, "alternatives": ["html", "css", "javascript", "web"]},
            "api": {"weight": 8, "alternatives": ["rest", "api", "restful"]},
            "english": {"weight": 10, "alternatives": ["english", "inglés"]}
        }
        
        self.experience_weights = {
            "Junior": 0.7,
            "Mid-level": 0.85,
            "Senior": 1.0
        }

        self.experience_levels = {
            (0, 3): "Junior",
            (3, 6): "Mid-level",
            (6, float('inf')): "Senior"
        }

    def _extract_years_experience_from_cv(self, cv_text: str) -> int:
        patterns = [
            r"(\d+)\+?\s*años?\s+de\s+experiencia",
            r"experiencia\s+de\s+(\d+)\+?\s*años?",
            r"con\s+(?:más\s+de\s+)?(\d+)\+?\s*años?\s+de\s+experiencia",
            r"(\d+)\+?\s*años?\s+de\s+experiencia\s+en",
            r"(\d+)\+?\s*years?\s+of\s+experience",
            r"experience\s+of\s+(\d+)\+?\s*years?",
            r"with\s+(?:more\s+than\s+)?(\d+)\+?\s*years?\s+experience",
            r"(\d+)\+?\s*years?\s+experience\s+in",
            r"(?:Desarrollador|Developer).+?(?:con|with)\s+(?:más\s+de\s+)?(\d+)\+?\s*años?"
        ]
        
        max_years = 0
        cv_text_lower = cv_text.lower()

        for pattern in patterns:
            matches = re.finditer(pattern, cv_text_lower)
            for match in matches:
                try:
                    years = int(match.group(1))
                    max_years = max(max_years, years)
                except (IndexError, ValueError):
                    continue
        try:
            
            date_ranges = re.finditer(r'(\d{4})\s*-\s*(\d{4})', cv_text)
            for date_range in date_ranges:
                start_year = int(date_range.group(1))
                end_year = int(date_range.group(2))
                years_of_exp = end_year - start_year
                max_years = max(max_years, years_of_exp)
        except (IndexError, ValueError):
            pass

        return max_years

    def _determine_experience_level(self, years: int) -> str:
        for (min_years, max_years), level in self.experience_levels.items():
            if min_years <= years < max_years:
                return level
        return "Senior" 

    def calculate_match(self, cv_analysis: Dict, job_requirements: Dict) -> Dict:
        score = 0
        missing_skills = []
        feedback = []
        language = job_requirements.get("language", "en")
        
        cv_years = self._extract_years_experience_from_cv(cv_analysis.get("cv_text", ""))
        required_years = job_requirements.get("min_years_experience", 0)
        
        if cv_years >= required_years:
            score += 30
            extra_years = cv_years - required_years
            if extra_years > 0:
                bonus_points = min(15, extra_years * 2)
                score += bonus_points
        else:
            feedback.append(
                f"Se requieren {required_years}+ años de experiencia (tienes {cv_years})" if language == "es"
                else f"{required_years}+ years of experience required (you have {cv_years})"
            )

        all_cv_skills = (
            cv_analysis["skills_analysis"]["backend_skills_found"] +
            cv_analysis["skills_analysis"]["frontend_skills_found"] +
            cv_analysis["skills_analysis"]["general_skills_found"]
        )
        
        for skill_name, skill_info in self.required_skills.items():
            skill_found = False
            for alternative in skill_info["alternatives"]:
                if any(s.lower() in alternative or alternative in s.lower() for s in all_cv_skills):
                    skill_found = True
                    score += skill_info["weight"]
                    break
            
            if not skill_found:
                missing_skills.append(skill_name.replace("_", " ").title())

        if "english" in job_requirements.get("required_skills", []):
            cv_english_level = self._detect_english_level(cv_analysis.get("cv_text", ""))
            required_english = job_requirements.get("required_english_level", "intermediate")
            
            if self._compare_english_levels(cv_english_level, required_english) < 0:
                feedback.append(
                    f"Se requiere nivel de inglés {required_english} (tienes {cv_english_level})" if language == "es"
                    else f"{required_english} English level required (you have {cv_english_level})"
                )
                score -= 10

        max_possible_score = 100
        match_percentage = min(100, int((score / max_possible_score) * 100))
        
        return {
            "match_percentage": match_percentage,
            "missing_skills": missing_skills,
            "feedback": feedback,
            "qualification_status": self._get_qualification_status(match_percentage, language),
            "years_of_experience": cv_years,
            "experience_level": self._determine_experience_level(cv_years)
        }

    def _detect_english_level(self, text: str) -> str:
        text = text.lower()
        if "advanced english" in text or "inglés avanzado" in text:
            return "advanced"
        elif "intermediate english" in text or "inglés intermedio" in text:
            return "intermediate"
        elif "basic english" in text or "inglés básico" in text:
            return "basic"
        return "intermediate" 

    def _compare_english_levels(self, cv_level: str, required_level: str) -> int:
        levels = {"basic": 1, "intermediate": 2, "advanced": 3}
        cv_score = levels.get(cv_level, 0)
        required_score = levels.get(required_level, 0)
        return cv_score - required_score

    def _get_qualification_status(self, percentage: int, language: str) -> str:
        if percentage >= 85:
            return "Altamente calificado" if language == "es" else "Highly qualified"
        elif percentage >= 70:
            return "Calificado" if language == "es" else "Qualified"
        else:
            return "Necesita mejoras" if language == "es" else "Needs improvement"

    def analyze_requirements(self, job_description: str) -> Dict:
        """Analiza los requisitos del puesto desde la descripción"""
        description_lower = job_description.lower()
        
        language = "es" if any(word in description_lower for word in ["años", "experiencia", "requisitos"]) else "en"
        
        years_pattern = r"(\d+)\+?\s*(?:years?|años?)(?:\s+(?:of|de))?\s+(?:experience|experiencia)"
        years_match = re.search(years_pattern, description_lower)
        min_years_experience = int(years_match.group(1)) if years_match else 0

        english_level = "basic"
        if "advanced english" in description_lower or "inglés avanzado" in description_lower:
            english_level = "advanced"
        elif "intermediate english" in description_lower or "inglés intermedio" in description_lower:
            english_level = "intermediate"

        required_skills = []
        for skill_name, skill_info in self.required_skills.items():
            for alternative in skill_info["alternatives"]:
                if alternative in description_lower:
                    required_skills.append(skill_name)
                    break

        return {
            "language": language,
            "min_years_experience": min_years_experience,
            "required_skills": required_skills,
            "required_english_level": english_level,
            "education_required": "degree" in description_lower or "título" in description_lower
        } 