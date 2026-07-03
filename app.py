import streamlit as st
import pandas as pd
import joblib
import time

# ------------------------------
# Load Model
# ------------------------------
model = joblib.load("employee_salary_model.pkl")

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💼",
    layout="wide"
)

# ------------------------------
# CSS
# ------------------------------
st.markdown("""
<style>

.main{
    background:#F7F9FC;
}

h1{
    color:#1565C0;
    text-align:center;
}

.stButton>button{
    width:100%;
    height:55px;
    background:#1565C0;
    color:white;
    font-size:18px;
    border-radius:10px;
}

.stButton>button:hover{
    background:#0D47A1;
}

</style>
""",unsafe_allow_html=True)

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("💼 Employee Salary Prediction")

st.sidebar.success("Algorithm : Linear Regression")

st.sidebar.info("Regression Project")

st.sidebar.write("Predict employee salary using Machine Learning.")

# ------------------------------
# Heading
# ------------------------------
st.title("💼 Employee Salary Prediction")

st.write("Predict the estimated annual salary based on employee profile.")

st.divider()

left,right=st.columns(2)

with left:

    experience = st.number_input(
        "Experience (Years)",
        min_value=0,
        max_value=40,
        value=5
    )

    skills = st.number_input(
        "Skills Count",
        min_value=0,
        max_value=30,
        value=8
    )

    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=2
    )

    education = st.selectbox(
        "Education Level",
        [
            "Bachelor",
            "Diploma",
            "High School",
            "Master",
            "PhD"
        ]
    )

    job_title = st.selectbox(
        "Job Title",
        [
            "Software Engineer",
            "Backend Developer",
            "Frontend Developer",
            "Business Analyst",
            "Cloud Engineer",
            "Cybersecurity Analyst",
            "Data Analyst",
            "Data Scientist",
            "DevOps Engineer",
            "Machine Learning Engineer",
            "Product Manager"
        ]
    )

with right:

    company = st.selectbox(
        "Company Size",
        [
            "Large",
            "Medium",
            "Small",
            "Startup"
        ]
    )

    industry = st.selectbox(
        "Industry",
        [
            "Technology",
            "Finance",
            "Government",
            "Healthcare",
            "Manufacturing",
            "Media",
            "Retail",
            "Telecom",
            "Education"
        ]
    )

    location = st.selectbox(
        "Location",
        [
            "USA",
            "Canada",
            "Germany",
            "India",
            "Netherlands",
            "Remote",
            "Singapore",
            "Sweden",
            "UK"
        ]
    )

    remote = st.selectbox(
        "Remote Work",
        [
            "No",
            "Yes"
        ]
    )

st.divider()

if st.button("💰 Predict Salary"):

    with st.spinner("Predicting Salary..."):
        time.sleep(1)

    feature_columns = [

        'experience_years',
        'skills_count',
        'certifications',

        'job_title_Backend Developer',
        'job_title_Business Analyst',
        'job_title_Cloud Engineer',
        'job_title_Cybersecurity Analyst',
        'job_title_Data Analyst',
        'job_title_Data Scientist',
        'job_title_DevOps Engineer',
        'job_title_Frontend Developer',
        'job_title_Machine Learning Engineer',
        'job_title_Product Manager',
        'job_title_Software Engineer',

        'education_level_Diploma',
        'education_level_High School',
        'education_level_Master',
        'education_level_PhD',

        'industry_Education',
        'industry_Finance',
        'industry_Government',
        'industry_Healthcare',
        'industry_Manufacturing',
        'industry_Media',
        'industry_Retail',
        'industry_Technology',
        'industry_Telecom',

        'company_size_Large',
        'company_size_Medium',
        'company_size_Small',
        'company_size_Startup',

        'location_Canada',
        'location_Germany',
        'location_India',
        'location_Netherlands',
        'location_Remote',
        'location_Singapore',
        'location_Sweden',
        'location_UK',
        'location_USA',

        'remote_work_No',
        'remote_work_Yes'
    ]

    input_data = {col:0 for col in feature_columns}

    input_data["experience_years"] = experience
    input_data["skills_count"] = skills
    input_data["certifications"] = certifications

    if f"job_title_{job_title}" in input_data:
        input_data[f"job_title_{job_title}"] = 1

    if f"education_level_{education}" in input_data:
        input_data[f"education_level_{education}"] = 1

    if f"industry_{industry}" in input_data:
        input_data[f"industry_{industry}"] = 1

    if f"company_size_{company}" in input_data:
        input_data[f"company_size_{company}"] = 1

    if f"location_{location}" in input_data:
        input_data[f"location_{location}"] = 1

    if f"remote_work_{remote}" in input_data:
        input_data[f"remote_work_{remote}"] = 1

    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    prediction = float(model.predict(input_df)[0])

    st.divider()

    st.subheader("💰 Salary Prediction Result")

    st.success(f"Estimated Annual Salary : ${prediction:,.2f}")

    salary_percent = min(prediction / 300000, 1.0)

    st.progress(salary_percent)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Estimated Salary",
            f"${prediction:,.2f}"
        )

    with col2:

        if prediction >= 180000:
            level = "Excellent ⭐"

        elif prediction >= 120000:
            level = "High 📈"

        elif prediction >= 70000:
            level = "Average 👍"

        else:
            level = "Entry Level 🌱"

        st.metric(
            "Salary Level",
            level
        )

    st.divider()

    st.subheader("👨‍💼 Employee Profile")

    profile = pd.DataFrame({

        "Experience":[experience],

        "Skills":[skills],

        "Certifications":[certifications],

        "Education":[education],

        "Job Title":[job_title],

        "Industry":[industry],

        "Company Size":[company],

        "Location":[location],

        "Remote Work":[remote]

    })

    st.dataframe(profile, use_container_width=True)

    st.divider()

    st.subheader("💡 Career Recommendations")

    if experience < 3:
        st.warning("Gain more industry experience.")

    if skills < 10:
        st.info("Improve your technical skills.")

    if certifications < 3:
        st.info("Complete professional certifications.")

    if education == "Bachelor":
        st.info("A Master's degree can improve salary opportunities.")

    if remote == "Yes":
        st.success("Remote work experience adds value to your profile.")

    if prediction >= 180000:

        st.success("Excellent profile. You are expected to receive a high salary package.")

    elif prediction >= 120000:

        st.success("Strong profile with very good salary potential.")

    elif prediction >= 70000:

        st.info("Good profile. Continue improving your skills and experience.")

    else:

        st.warning("Focus on gaining experience, certifications and technical skills.")

    st.divider()

    st.caption(
        "Machine Learning Project | Linear Regression | Employee Salary Prediction"
    )