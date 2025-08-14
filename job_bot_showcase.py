import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Job Bot Showcase", page_icon="🤖", layout="wide")

# Header
st.image("your_logo.png", width=100)  # Optional
st.title("Job Application Automation Bot 🤖")
st.markdown("A visual walkthrough of how Vikrant's bot automates job applications across major platforms.")

# Sidebar: Bot Simulation Settings
with st.sidebar:
    st.header("🔧 Bot Simulation")
    platform = st.multiselect("Platforms", ["LinkedIn", "Naukri", "Indeed"], default=["LinkedIn"])
    keywords = st.text_input("Keywords", "Data Analyst, Python, Power BI")
    location = st.text_input("Location", "Mumbai, Remote")
    st.button("Simulate Bot Run 🚀")

# Simulated Job Feed
st.subheader("📋 Sample Job Listings")
job_df = pd.DataFrame({
    "Job Title": ["Data Analyst", "BI Developer"],
    "Company": ["ABC Corp", "XYZ Ltd"],
    "Location": ["Mumbai", "Remote"],
    "Apply Link": ["https://example.com/apply1", "https://example.com/apply2"]
})
st.dataframe(job_df)

# Application Summary
st.subheader("📊 Application Summary")
st.metric("Jobs Applied", 45)
st.metric("Skipped", 12)
st.metric("Errors", 3)

# Footer
st.markdown("---")
st.markdown("**Built by Vikrant Thenge** | [GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)")
st.markdown("Tech Stack: 🐍 Python | 📊 Streamlit | 🤖 Selenium | ☁️ AWS | 📈 Power BI")
