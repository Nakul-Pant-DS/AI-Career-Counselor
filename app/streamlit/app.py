import requests
import streamlit as st

# ==========================================================
# Configuration
# ==========================================================

import os

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8000/api/v1"
)

st.set_page_config(
    page_title="AI Career Counselor",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# Session State
# ==========================================================

if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

if "career_result" not in st.session_state:
    st.session_state.career_result = None

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🤖 AI Career Counselor")

    st.success("Backend Connected")

    st.divider()

    st.markdown("### Version")
    st.info("v1.0 MVP")

    st.divider()

    st.markdown("### Features")

    st.write("✅ Resume Upload")
    st.write("✅ Resume Parsing")
    st.write("✅ AI Career Analysis")

# ==========================================================
# Header
# ==========================================================

st.title("🤖 AI Career Counselor")

st.caption(
    "Enterprise AI Powered Career Analysis Platform"
)

st.divider()

# ==========================================================
# Resume Upload
# ==========================================================

st.header("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("📤 Upload Resume", use_container_width=True):

        with st.spinner("Uploading Resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            try:

                response = requests.post(
                    f"{API_BASE_URL}/resume/upload",
                    files=files
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state.resume_uploaded = True

                    st.success("✅ Resume Uploaded Successfully!")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("Pages", data["pages"])

                    with col2:
                        st.metric("Characters", data["characters"])

                    with st.expander("Resume Preview"):

                        st.write(data["preview"])

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(str(e))

st.divider()

# ==========================================================
# Career Analysis
# ==========================================================

st.header("💼 Career Analysis")

question = st.text_area(

    "Ask a Career Question",

    value="Am I suitable for an AI Engineer role?"

)

analyze = st.button(
    "🚀 Analyze Career",
    use_container_width=True
)

if analyze:

    if not st.session_state.resume_uploaded:

        st.warning("Please upload your resume first.")

    else:

        with st.spinner("Analyzing Career..."):

            try:

                response = requests.post(

                    f"{API_BASE_URL}/career-analysis",

                    json={
                        "question": question
                    }

                )

                if response.status_code == 200:

                    st.session_state.career_result = response.json()

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(str(e))

# ==========================================================
# Results
# ==========================================================

if st.session_state.career_result is not None:

    result = st.session_state.career_result

    st.divider()

    st.header("📊 Career Analysis Report")

    st.metric(
        "Suitability Score",
        f'{result["suitability_score"]}%'
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🎯 Recommended Roles")

        for role in result["recommended_roles"]:
            st.success(role)

    with col2:

        st.subheader("💪 Strengths")

        for skill in result["strengths"]:
            st.info(skill)

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("📚 Missing Skills")

        for skill in result["missing_skills"]:
            st.warning(skill)

    with col4:

        st.subheader("🛣 Learning Roadmap")

        for step in result["learning_roadmap"]:
            st.write("✅", step)

    st.divider()

    st.subheader("📝 Summary")

    st.success(result["summary"])
