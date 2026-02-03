# placement.py
# ---------------- CORE PLACEMENT LOGIC ----------------

def normalize_skills(skills):
    return set(skill.strip().lower() for skill in skills if skill.strip())


def skills_taught_upto_year(student_year, curriculum):
    year_order = ["1st Year", "2nd Year", "3rd Year", "4th Year"]

    if student_year not in year_order:
        return set()

    allowed_years = year_order[: year_order.index(student_year) + 1]

    taught_skills = set()
    for year in allowed_years:
        for subject in curriculum.get(year, []):
            taught_skills.update(subject.get("skills", []))

    return normalize_skills(taught_skills)


def evaluate_company(student, company, curriculum):
    """
    Deterministic, explainable placement evaluation.
    NO ML. NO AI. NO UI.
    """

    reasons = []

    # ---------------- CGPA CHECK ----------------
    if student["cgpa"] < company["min_cgpa"]:
        return {
            "eligible": False,
            "fit_score": 0,
            "missing_skills": [],
            "reasons": [
                f"CGPA {student['cgpa']} is below required {company['min_cgpa']}"
            ],
        }

    # ---------------- SKILL MATCHING ----------------
    student_skills = normalize_skills(student["skills"])
    company_skills = normalize_skills(company["skills"])

    matched_skills = student_skills & company_skills
    missing_skills = company_skills - student_skills

    # ---------------- CURRICULUM RELAXATION ----------------
    taught_skills = skills_taught_upto_year(student["year"], curriculum)

    penalizable_missing = missing_skills & taught_skills
    non_penalizable_missing = missing_skills - taught_skills

    # ---------------- FIT SCORE ----------------
    if len(company_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / len(company_skills)) * 60

    project_score = min(student["projects"] * 10, 20)
    experience_score = min(student["experience_months"], 20)

    fit_score = round(
        min(skill_score + project_score + experience_score, 100), 2)

    # ---------------- EXPLANATION ----------------
    if penalizable_missing:
        reasons.append(
            "Missing core skills currently taught: "
            + ", ".join(penalizable_missing)
        )

    if non_penalizable_missing:
        reasons.append(
            "Some required skills are taught in later years and are not penalized yet."
        )

    if fit_score >= 70:
        reasons.append("Strong overall fit for this company.")
    elif fit_score >= 40:
        reasons.append("Moderate fit. Improvement recommended.")
    else:
        reasons.append("Low fit. Significant preparation required.")

    return {
        "eligible": True,
        "fit_score": fit_score,
        "missing_skills": list(missing_skills),
        "reasons": reasons,
    }
