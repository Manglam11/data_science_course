import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from ollama import Client


client = Client(host="http://localhost:11434")

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload you resume (PDF)", type="pdf")

df = pd.read_csv("job_dataset.csv")

if uploaded_file:
    st.success("File uploaded successfully")

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Resume Text:")
    st.write(text[:1000])

    st.subheader("🎯 Select Job Role")
    job_titles = df["Title"].dropna().unique()
    selected_job = st.selectbox("Choose a role:", job_titles)

    st.divider()
    if st.button("Analyze Resume"):
        if text.strip() == "":
            st.warning("No text found in resume.")
        else:
            with st.spinner("Analying you resume..."):
                job_data = df[df["Title"] == selected_job].iloc[0]
                job_description = job_data["Responsibilities"]
#                 prompt = f"""
# Analyze the following resume:
# {text}
# Give:
# 1. Strengths
# 2. Weaknesses
# 3. Suggestions for improvement
# 4. Score out of 10
# """
                prompt = f"""
Compare this resume with the job description.
Resume:
{text}

Job Description:
{job_description}
Give:
1. Matching skills
2. Missing skills
3. How well the candidate fits this role
4. Suggestions to improve
5. Score out of 10
"""
                response = client.chat(
                    model = "kimi-k2.5:cloud",
                    messages=[
                        {"role": "user",
                         "content": prompt}
                    ]
                )
                st.subheader("📊 AI Feedback")
                st.write(response["message"]["content"])

        st.divider()
        st.subheader("🛠 Detected Skills")

        # skills_list = ["Python", "Flask", "Rest API", "GitHub", "Machine Learning", "Data Analyst"]
        # job_data = df[df["Title"] == selected_job].iloc[0]
        skills_string = job_data["Skills"]
        skills_list = [skill.strip() for skill in skills_string.split(";")]
        # skills_list = ["Python", "Flask", "Rest API", "GitHub", "Machine Learning", "Data Analyst"]
        found_skills = []

        for skill in skills_list:
            if skill.lower() in text.lower():
                found_skills.append(skill)
        if found_skills:
            st.success(f"Skills found: {', '.join(found_skills)}")
        else:
            st.warning("No predefined skills detected")

    # st.divider()
    # st.subheader("📊 Resume Score")
    #
    # score = 0
    # if len(text) > 1000:
    #     score += 2
    #
    # if len(found_skills) >= 3:
    #     score += 3
    #
    # if "project" in text.lower():
    #     score += 2
    #
    # if "experience" in text.lower():
    #     score += 3
    # st.write(f"Your Resume Score: {score}/10")