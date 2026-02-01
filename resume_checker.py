# logic/resume_checker.py
import pdfplumber
import re


def extract_resume_text(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return normalize_text(text)


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+.# ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_skills(resume_text, known_skills):
    found_skills = set()
    for skill in known_skills:
        if skill in resume_text:
            found_skills.add(skill)
    return found_skills


def check_sections(resume_text):
    sections = {
        "education": False,
        "skills": False,
        "projects": False,
        "experience": False
    }

    for section in sections:
        if section in resume_text:
            sections[section] = True

    return sections


def compute_resume_score(found_skills, required_skills, sections):
    score = 0
    explanation = []

    # Skill match (50%)
    skill_score = (len(found_skills) / max(1, len(required_skills))) * 50
    score += skill_score

    # Sections (50%)
    section_score = sum(sections.values()) / len(sections) * 50
    score += section_score

    if skill_score < 25:
        explanation.append("Low skill match with target role.")
    if not sections["projects"]:
        explanation.append("Projects section missing or weak.")

    return round(score, 2), explanation


def analyze_resume(uploaded_file, known_skills, required_skills):
    resume_text = extract_resume_text(uploaded_file)

    found_skills = extract_skills(resume_text, known_skills)
    missing_skills = set(required_skills) - found_skills

    sections = check_sections(resume_text)

    score, explanation = compute_resume_score(
        found_skills, required_skills, sections
    )

    return {
        "resume_score": score,
        "found_skills": list(found_skills),
        "missing_skills": list(missing_skills),
        "sections": sections,
        "explanation": explanation
    }


def analyze_resume_base(uploaded_file):
    resume_text = extract_resume_text(uploaded_file)
    found_skills = extract_skills(resume_text, known_skills)
    sections = check_sections(resume_text)

    return {
        "resume_text": resume_text,
        "found_skills": found_skills,
        "sections": sections

    }


def match_resume_to_company(resume_data, company_skills):
    found = resume_data["found_skills"]
    required = set(company_skills)

    matched = found & required
    missing = required - found

    match_percent = (len(matched) / max(1, len(required))) * 100

    return {
        "match_percent": round(match_percent, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }
