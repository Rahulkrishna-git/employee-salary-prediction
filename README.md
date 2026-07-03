# 💼 Employee Salary Prediction using Machine Learning

## 📌 Project Overview

The Employee Salary Prediction project is a Machine Learning web application developed using Python and Streamlit. The application predicts the estimated annual salary of an employee based on professional details such as experience, education, job role, skills, certifications, company size, industry, work location, and remote work preference.

The project applies Linear Regression to learn relationships between employee attributes and salary, providing quick and accurate salary predictions through an interactive user interface.

---

## 🎯 Objectives

- Predict employee annual salary using Machine Learning.
- Build a simple and user-friendly web application.
- Compare multiple regression algorithms.
- Select the best-performing model.
- Deploy the model using Streamlit.

---

## 📂 Dataset Information

The dataset contains approximately **250,000 employee records** with the following attributes:

- Job Title
- Experience Years
- Education Level
- Skills Count
- Industry
- Company Size
- Location
- Remote Work
- Certifications
- Salary (Target Variable)

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## 🤖 Machine Learning Workflow

1. Import Libraries
2. Load Dataset
3. Data Exploration
4. Data Cleaning
5. Handle Missing Values
6. Remove Duplicates
7. One-Hot Encoding
8. Feature Selection
9. Train-Test Split
10. Train Multiple Models
11. Compare Model Performance
12. Select Best Model
13. Save Model using Joblib
14. Build Streamlit Web Application

---

## 📊 Models Compared

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Final Selected Model

**Linear Regression**

Reason:
- Highest R² Score
- Fast Prediction
- Simple and Efficient
- Best performance on this dataset

---

## 📈 Evaluation Metrics

The following metrics were used:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 💻 Application Features

- Professional Streamlit User Interface
- Employee Profile Input Form
- Salary Prediction
- Employee Details Summary
- Salary Level Indicator
- Career Improvement Suggestions
- Responsive Layout

---

## 📁 Project Structure

```
Employee-Salary-Prediction/
│
├── app.py
├── employee_salary_model.pkl
├── job_salary_prediction_dataset.csv
├── Untitled.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Employee-Salary-Prediction.git
```

Move into the project directory

```bash
cd Employee-Salary-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Screens

- Home Page
- Employee Details Form
- Salary Prediction Result
- Career Recommendation Section

---

## 🚀 Future Enhancements

- XGBoost Regression
- LightGBM Regression
- Salary Trend Visualization
- PDF Report Generation
- User Authentication
- Cloud Deployment
- Model Explainability using SHAP

---

## 📚 Learning Outcomes

This project demonstrates:

- Data Preprocessing
- Feature Engineering
- Regression Algorithms
- Model Evaluation
- Model Serialization
- Streamlit Deployment
- End-to-End Machine Learning Pipeline

---

## 👨‍💻 Author

**Rahul krishna**

B.Tech Information Technology

Machine Learning Mini Project

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.
