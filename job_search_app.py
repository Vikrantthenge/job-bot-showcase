import streamlit as st
import pandas as pd
import requests
from PIL import Image

# --- Page Setup ---
st.set_page_config(page_title="Job Search Bot", layout="wide")

# --- Logo + Theme Phrase ---
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- Load and encode logo ---
try:
    logo = Image.open("your_logo.png")
    buffered = BytesIO()
    logo.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # --- Display logo + phrase side-by-side ---
    st.markdown(f"""
        <div style='display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 1.5rem;'>
            <img src='data:image/png;base64,{img_base64}' width='60'>
            <span style='font-size: 20px; font-weight: 600; color: #8B0000;'>Your Data Career Starts Here</span>
        </div>
    """, unsafe_allow_html=True)

except FileNotFoundError:
    st.warning("Logo file 'your_logo.png' not found. Please add it to the app folder.")

# --- Logo ---

#  try:
   #  logo = Image.open("your_logo.png")
    #  st.image(logo, width=150)
#  except FileNotFoundError:
   #  st.warning("Logo file 'your_logo.png' not found. Please add it to the app folder.")

# --- Title & Tagline ---
#st.title("Data Job Finder + Resume Uploader")
st.markdown("""
    <div style='text-align: center; font-size: 40px; font-weight: 600; color: #8B0000; margin-bottom: 0.5rem;'>
        🚀 Data Job Finder + Resume Uploader
    </div>
    <div style='text-align: center; font-size: 16px; color: #333333; margin-bottom: 1.5rem;'>
        Discover curated data job listings and upload your resume with ease. This app streamlines your job search by combining smart filtering, intuitive design, and recruiter-ready presentation — all in one place.
    </div>
""", unsafe_allow_html=True)


st.markdown("##### *Your personalized job search assistant — built for speed, clarity, and results.*")

# --- Sidebar Filters ---
st.sidebar.header("🎯 Job Search Filters")
keywords = st.sidebar.text_input("Job Title", value="Data Analyst")
location = st.sidebar.text_input("Location", value="India")
num_pages = st.sidebar.slider("Pages to Search", 1, 5, 1)
st.sidebar.markdown("**Tech Stack:** Python · Streamlit · RapidAPI · Resume Parsing · Automation")

# --- Resume Upload ---
st.subheader("📤 Upload Your Resume")
resume = st.file_uploader("Upload PDF Resume", type=["pdf"])
if resume:
    st.success("Resume uploaded successfully!")
    # Optional: parse resume for keyword matching

# --- Fetch Jobs Function ---
def fetch_jobs(keywords, location, num_pages):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": f"{keywords} in {location}", "num_pages": str(num_pages)}
    headers = {
        "X-RapidAPI-Key": "71a00e1f1emsh5f78d93a2205a33p114d26jsncc6534e3f6b3",  # Replace with your actual RapidAPI key
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

# --- Job Search Trigger ---
if st.sidebar.button("Search Jobs"):
    with st.spinner("Fetching jobs..."):
        job_df = fetch_jobs(keywords, location, num_pages)
        if not job_df.empty:
            st.subheader("💼 Job Listings")
            for i, row in job_df.iterrows():
                st.markdown(f"**{row['Job Title']}** at *{row['Company']}* — {row['Location']}")
                st.markdown(f"[Apply Now]({row['Apply Link']})", unsafe_allow_html=True)
                st.markdown("---")
        else:
            st.warning("No jobs found. Try different keywords or location.")

# --- Auto-Apply Simulation ---
if st.button("🚀 Auto-Apply to All"):
    if resume:
        st.success("Bot applied to all matching jobs ✅ (simulated)")
    else:
        st.error("Please upload your resume first.")

# Add styled copyright footer
st.markdown("""
   <hr style="margin-top: 2rem; margin-bottom: 0.5rem;">
    <div style='text-align: center; font-size: 12px; color: #8B0000;'>
        © 2025 VIKRANT THENGE. All rights reserved.
    </div>
""", unsafe_allow_html=True)