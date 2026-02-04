import nltk
import streamlit as st
import pickle
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

#loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open("label_encoder.pkl", "rb")) 

def cleanResume(resume_text):
    cleantxt = re.sub('http\S+\s*', ' ', resume_text)  # remove URLs
    cleantxt = re.sub('RT|cc', ' ', cleantxt)  # remove RT and cc
    cleantxt = re.sub('#\S+', ' ', cleantxt)  # remove hashtags
    cleantxt = re.sub('@\S+', ' ', cleantxt)  # remove mentions
    cleantxt = re.sub('[%$&*<>#@()~`/-:]', ' ', cleantxt)  # remove special characters
    cleantxt = re.sub(r'[^\x00-\x7F]+', ' ', cleantxt)  # remove non-ASCII characters
    cleantxt = re.sub('\s+', ' ', cleantxt)  # remove extra whitespace
    return cleantxt

#web app
def main():
   st.title("Resume Screening Application")
   uploaded_file = st.file_uploader("Upload Resume", type=["pdf","docx","txt"])

   if uploaded_file is not None:
        try:
             resume_bytes = uploaded_file.read()
             resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
              resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = cleanResume(resume_text)
        input_feature = tfidf.transform([cleaned_resume])
        prediction_id = clf.predict(input_feature)[0]
        st.write("Predicted id :", prediction_id)
        prediction_label = le.inverse_transform([prediction_id])[0]
        st.subheader("Predicted Job Category:")
        st.write(prediction_label)

#python main 
if __name__ == '__main__':
       main()   