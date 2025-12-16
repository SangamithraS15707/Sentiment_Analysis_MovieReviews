import streamlit as st
import joblib
import re
from bs4 import BeautifulSoup

# -----------------------------
# Load saved model and CountVectorizer
# -----------------------------
model = joblib.load("sentiment_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# -----------------------------
# Text preprocessing function
# -----------------------------
def preprocess(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Sentiment Analysis", layout="centered")

st.title("🎬 Movie Review Sentiment Analysis")
st.write("Enter a movie review and predict its sentiment using Naïve Bayes.")

review_input = st.text_area("Movie Review", height=150)

if st.button("Predict Sentiment"):
    if review_input.strip() == "":
        st.warning("Please enter a review")
    else:
        clean_review = preprocess(review_input)
        review_vec = vectorizer.transform([clean_review])
        prediction = model.predict(review_vec)[0]

        if prediction == 1:
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")

st.markdown("---")
st.caption("Model: Multinomial Naïve Bayes | Features: Bag of Words")
