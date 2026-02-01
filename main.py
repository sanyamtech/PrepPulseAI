import streamlit as st


import json

with open("data/companies.json") as f:
    COMPANIES = json.load(f)


from resume_checker import (
    analyze_resume_base,
    match_resume_to_company
)


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Placement Guidance System",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 5px;'>
        Placement Guidance System
    </h1>
    <p style='text-align: center; color: gray; margin-top: 0;'>
        Curriculum-aware career guidance for students
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- TOP NAVIGATION ----------------
tabs = st.tabs(
    ["🏠 Home", "📄 Resume Checker", "🏢 Companies", "🎯 Placement", "📘 Study"]
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("Student Profile")

year = st.sidebar.selectbox(
    "Academic Year",
    ["Select", "1st Year", "2nd Year", "3rd Year", "4th Year"]
)

cgpa = st.sidebar.number_input("CGPA", 0.0, 10.0, step=0.1)
skills = st.sidebar.text_input("Skills (comma separated)")
experience = st.sidebar.number_input("Experience (months)", 0, 60)

# ======================================================
# HOME
# ======================================================
with tabs[0]:
    st.subheader("Welcome")

    if year == "Select":
        st.info(
            "Select your academic year from the sidebar to activate personalization.")
    else:
        st.success(f"Personalized mode active for **{year}** students.")

    st.write(
        """
        This platform helps students understand:
        - where they stand today  
        - what companies expect  
        - what to study next (without violating curriculum flow)  
        """
    )

# ======================================================
# RESUME CHECKER
# ======================================================
with tabs[1]:
    st.subheader("Resume Checker")

    uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    KNOWN_SKILLS = [
        "c", "python", "java", "sql", "dbms",
        "data structures", "algorithms",
        "html", "css", "javascript"
    ]

    REQUIRED_SKILLS = ["python", "sql"]  # example role/company

    if uploaded:
        st.success("Resume uploaded successfully.")

        KNOWN_SKILLS = [
            "c", "python", "java", "sql", "dbms",
            "data structures", "algorithms",
            "html", "css", "javascript"
        ]

        resume_data = analyze_resume_base(uploaded, KNOWN_SKILLS)

        st.subheader("Resume Skills Detected")
        st.write(list(resume_data["found_skills"]))

        st.subheader("Company-wise Match")

        for company in COMPANIES:
            result = match_resume_to_company(
                resume_data,
                company["skills"]
            )

            st.markdown(f"### {company['name']}")
            st.metric("Skill Match", f"{result['match_percent']}%")
            st.write("Missing Skills:", result["missing_skills"])
            st.divider()

    else:
        st.warning("Upload a resume to begin analysis.")

# ======================================================
# COMPANIES
# ======================================================
with tabs[2]:
    st.subheader("Companies on Campus")

    st.write("Explore company eligibility, packages, and hiring process.")

    st.table({
        "Company": ["ABC Tech", "XYZ Corp"],
        "Min CGPA": [7.0, 6.5],
        "Package (LPA)": [10, 6]
    })

# ======================================================
# PLACEMENT
# ======================================================
with tabs[3]:
    st.subheader("Placement Readiness")

    if year == "Select":
        st.warning("Select your academic year from the sidebar.")
    else:
        col1, col2, col3 = st.columns(3)

        col1.metric("Fit Score", "72%")
        col2.metric("Placement Probability", "0.64")
        col3.metric("Resume Strength", "Medium")

        st.info("Scores are adjusted based on your academic year and curriculum.")

# ======================================================
# STUDY
# ======================================================
with tabs[4]:
    st.subheader("Study Guidance")

    if year == "Select":
        st.warning("Select your academic year to view roadmap.")
    else:
        st.write(f"Recommended focus areas for **{year}**:")

        if year == "1st Year":
            st.write("- Programming fundamentals\n- Math & logic\n- Exploration")
        elif year == "2nd Year":
            st.write("- DSA\n- OOPS\n- Mini projects")
        elif year == "3rd Year":
            st.write("- OS, CN\n- Internships\n- Resume building")
        elif year == "4th Year":
            st.write("- SQL & system design\n- Interview prep\n- Company targeting")


# from google import genai

# # ⚠️ TEMPORARY: hard-coded API key (DO NOT COMMIT THIS)
# API_KEY = "AIzaSyA8q-u9b6qqm8DfM5X-CYlDpDN308ZDwcE"

# client = genai.Client(api_key=API_KEY)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="hello gemini "
# )

# print(response.text)
