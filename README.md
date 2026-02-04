# 🧠 Intelligent Resume Screening & Job Matching System

## 📌 Overview
Recruiters often spend hours manually screening resumes, which is time-consuming and prone to bias.  
This project builds an **AI-powered Resume Screening and Job Matching System** that automatically analyzes resumes and classifies them into relevant job categories using **Natural Language Processing (NLP)** and **Machine Learning**.

The system helps streamline the recruitment process by intelligently understanding resume content instead of relying on keyword matching.

---

## 🎯 Objectives
- Automate resume screening using NLP techniques
- Classify resumes into predefined job categories
- Reduce manual effort and human bias in hiring
- Provide a scalable and efficient resume analysis solution

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries & Tools:**
  - Pandas, NumPy
  - Scikit-learn
  - NLTK
  - TF-IDF Vectorizer
  - Streamlit (for UI)
- **Version Control:** Git & GitHub

---

## 🧩 Project Workflow
1. **Data Collection**
   - Resume dataset containing multiple job categories

2. **Text Preprocessing**
   - Cleaning resumes using regex
   - Removing URLs, special characters, stopwords
   - Lowercasing and normalization

3. **Feature Extraction**
   - TF-IDF Vectorization to convert text into numerical features

4. **Label Encoding**
   - Converting job categories into numerical labels
   - Maintaining reverse mapping using `LabelEncoder`

5. **Model Training**
   - Training a supervised ML classifier on resume features

6. **Prediction**
   - Predicting job category for unseen resumes
   - Mapping predicted labels back to category names

7. **Deployment**
   - Interactive web app built using Streamlit

---

## 🚀 How to Run the Project

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/your-username/Intelligent-Resume-Screening-Job-Matching-System.git
cd Intelligent-Resume-Screening-Job-Matching-System
