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

### 🔹 2. Create & Activate Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

### 🔹 3. Install Dependencies

Install the required libraries manually:

```bash
pip install numpy pandas scikit-learn nltk streamlit matplotlib seaborn



### 🔹 4. Run the Streamlit App
streamlit run app.py


⚠️ Important Note
Trained model files (clf.pkl, tfidf.pkl, label_encoder.pkl) are not included in this repository due to GitHub’s file size limitations.


➡️ To generate them:
Run the training notebook/script provided in the project
Models will be created locally and used automatically by the app
This follows standard machine learning project practices.
