# app/main_app.py
import streamlit as st
from core.parser import extract_text_from_pdf, extract_text_from_txt
from core.scoring import compute_scores

# Example skills database
DEFAULT_SKILLS = ["python", "java", "sql", "machine learning", "deep learning", "flask", "django"]

st.title("📄 Resume Analyzer")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "txt"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "txt"])

if st.button("Analyze") and resume_file and jd_file:
    # Save uploads to temp
    with open("data/tmp_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    with open("data/tmp_jd.pdf", "wb") as f:
        f.write(jd_file.read())

    # Parse files
    resume_text = extract_text_from_pdf("data/tmp_resume.pdf") if resume_file.name.endswith("pdf") \
        else extract_text_from_txt("data/tmp_resume.txt")

    jd_text = extract_text_from_pdf("data/tmp_jd.pdf") if jd_file.name.endswith("pdf") \
        else extract_text_from_txt("data/tmp_jd.txt")

    # Compute scores
    scores = compute_scores(resume_text, jd_text, DEFAULT_SKILLS)

    st.subheader("Results")
    st.json(scores)
