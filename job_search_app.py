import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Job Search Bot", layout="wide")
st.title("🔍 Data Job Finder + Resume Uploader")

# --- Sidebar Inputs ---
st.sidebar.header("Search Filters")
keywords = st.sidebar.text_input("Job Title", value="Data Analyst")
location = st.sidebar.text_input("Location", value="India")
num_pages = st.sidebar.slider("Pages to Search", 1, 5, 1)

# --- Resume Upload ---
st.subheader("📄 Upload Your Resume")
resume = st.file_uploader("Upload PDF Resume", type=["pdf"])
if resume:
    st.success("Resume uploaded successfully!")
    # Optional: parse resume for keyword matching

# --- Fetch Jobs ---
def fetch_jobs(keywords, location, num_pages):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": f"{keywords} in {location}", "num_pages": str(num_pages)}
    headers = {
        "X-RapidAPI-Key": "your_a71a00e1f1emsh5f78d93a2205a33p114d26jsncc6534e3f6b3",  # Replace with your actual key
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    jobs = [{
        "Job Title": job["job_title"],
        "Company": job["employer_name"],
        "Location": job["job_city"],
        "Apply Link": job["job_apply_link"]
    } for job in data.get("data", [])]
    return pd.DataFrame(jobs)

# --- Display Jobs ---
if st.sidebar.button("Search Jobs"):
    with st.spinner("Fetching jobs..."):
        job_df = fetch_jobs(keywords, location, num_pages)
        if not job_df.empty:
            st.subheader("📋 Job Listings")
            for i, row in job_df.iterrows():
                st.markdown(f"**{row['Job Title']}** at *{row['Company']}* — {row['Location']}")
                st.markdown(f"[Apply Now]({row['Apply Link']})", unsafe_allow_html=True)
                st.markdown("---")
        else:
            st.warning("No jobs found. Try different keywords or location.")

# --- Simulate Auto-Apply ---
if st.button("🚀 Auto-Apply to All"):
    if resume:
        st.success("Bot applied to all matching jobs ✅ (simulated)")
    else:
        st.error("Please upload your resume first.")
