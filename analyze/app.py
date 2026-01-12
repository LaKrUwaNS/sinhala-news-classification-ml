import os
import joblib
import streamlit as st

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Sinhala News Classifier",
    layout="centered"
)

# --------------------------------------------------
# High-contrast CSS (FIXES VISIBILITY ISSUE)
# --------------------------------------------------
st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #0f172a;
    color: #f8fafc;
}

/* Main container spacing */
.block-container {
    padding-top: 2rem;
}

/* Headings */
h1, h2, h3 {
    color: #f8fafc !important;
}

/* Info box */
.info-box {
    background-color: #1e293b;
    color: #e5e7eb;
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    font-size: 16px;
}

/* Labels */
label {
    color: #f8fafc !important;
    font-weight: 600;
}

/* Inputs */
input, textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 8px !important;
}

/* Buttons */
.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    font-size: 16px;
    padding: 0.6rem 1.2rem;
}

.stButton button:hover {
    background-color: #1d4ed8;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load trained model files (SAFE PATH)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "news_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "tfidf_vectorizer.pkl"))
label_encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

# --------------------------------------------------
# UI Header
# --------------------------------------------------
st.title("📰 Sinhala News Classifier")

st.markdown("""
<div class="info-box">
<b>How it works:</b><br>
Enter the Sinhala news title and description.  
The AI model will instantly predict the most relevant news category.
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# User Inputs
# --------------------------------------------------
title = st.text_input(
    "📝 News Title",
    placeholder="Enter Sinhala news title"
)

description = st.text_area(
    "📄 News Description",
    placeholder="Enter Sinhala news description",
    height=150
)

# --------------------------------------------------
# Prediction Function
# --------------------------------------------------
def predict_category(title, description):
    text = title + " " + description
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return label_encoder.inverse_transform(prediction)[0]

# --------------------------------------------------
# Predict Button
# --------------------------------------------------
if st.button("🔍 Predict Category"):
    if not title.strip() or not description.strip():
        st.warning("Please enter both title and description.")
    else:
        category = predict_category(title, description)
        st.success(f"✅ Predicted Category: **{category}**")
