# Movie Review Sentiment Analysis App

This is a **Streamlit web application** that predicts the sentiment of movie reviews as **Positive** or **Negative** using a **Multinomial Naïve Bayes classifier** with **Bag of Words (CountVectorizer)** features.

---

## Features

* Input a movie review and get a sentiment prediction in real-time.
* Handles raw HTML tags and noisy text with preprocessing.
* Clean and simple Streamlit interface.
* Persists trained model and vectorizer using `joblib`.

---

## Installation

1. Clone the repository or download the files.
2. Make sure the following files are present in the same folder:

   * `app.py` (Streamlit app)
   * `sentiment_model.joblib` (trained MultinomialNB model)
   * `vectorizer.joblib` (CountVectorizer for Bag of Words)
   * `requirements.txt`
3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

Run the Streamlit app using:

```bash
streamlit run app.py
```

This will open the app in your default browser.

---

## Usage

1. Enter a movie review in the text area.
2. Click the **Predict Sentiment** button.
3. The app will display:

   * ✅ Positive Review
   * ❌ Negative Review

### Example Reviews

* **Positive:** "I absolutely loved this movie! The story and acting were amazing."
* **Negative:** "This movie was terrible. The plot made no sense and I do not recommend it."

---

## Preprocessing

* HTML tags removed using **BeautifulSoup**
* Lowercasing all text
* Removing non-alphabetic characters using **regex**

---

## Model Details

* **Classifier:** Multinomial Naïve Bayes
* **Feature Extraction:** CountVectorizer (Bag of Words)
* **Accuracy:** ~83%

---

## License

This project is for educational and demonstration purposes.
