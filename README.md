# 📰 Sinhala News Category Classification & Data Analysis

> A machine learning project for classifying Sinhala-language news articles into predefined categories using traditional ML techniques

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)
![Status](https://img.shields.io/badge/Status-Educational-green.svg)

## 🌟 Overview

This educational project demonstrates a complete machine learning workflow for analyzing and classifying Sinhala-language news articles from Hiru News. The system categorizes news into six distinct categories: **Politics**, **Crime**, **International**, **Sports**, **Weather**, and **Other**.

The project showcases ethical web scraping practices, comprehensive exploratory data analysis, traditional machine learning techniques, and an interactive user interface for real-time predictions.

## ✨ Features

- **Ethical Web Scraping**: Responsible data collection from publicly accessible Hiru News listing pages
- **Comprehensive EDA**: Detailed exploratory data analysis with visualizations and insights
- **Text Processing Pipeline**: Advanced Sinhala text preprocessing and TF-IDF feature extraction
- **ML Classification**: Logistic Regression model for accurate category prediction
- **Interactive UI**: Streamlit-based web interface for real-time news classification
- **Reusable Models**: Trained models saved as `.pkl` files for easy deployment
- **Detailed Documentation**: Complete analytical report in Jupyter Notebook format

## 📊 Project Workflow

```
Data Collection → Exploratory Analysis → Text Preprocessing → 
Feature Extraction → Model Training → Evaluation → Deployment
```

### 1. Data Collection
- Scraped publicly available news headlines and summaries from Hiru News
- Focused on publicly accessible listing pages only
- No access to restricted or paywalled content

### 2. Exploratory Data Analysis
- Category distribution analysis
- Publication trends over time
- Content length and characteristics
- Word frequency analysis
- Temporal patterns in news coverage

### 3. Machine Learning Pipeline
- Text preprocessing tailored for Sinhala language
- TF-IDF vectorization for feature extraction
- Logistic Regression classifier training
- Model evaluation and performance metrics
- Model serialization using Joblib

### 4. Deployment
- Interactive Streamlit web application
- Real-time category prediction
- User-friendly interface for testing

## 🛠️ Technologies & Tools

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **Web Scraping** | Selenium |
| **Data Analysis** | Pandas, NumPy, Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn |
| **Model Persistence** | Joblib |
| **Notebook** | Jupyter Notebook |
| **Web Interface** | Streamlit |

## 📁 Project Structure

```
sinhala-news-classifier/
│
├── data/
│   ├── raw/                    # Raw scraped data
│   └── processed/              # Cleaned and preprocessed data
│
├── notebooks/
│   └── EDA_Report.ipynb        # Comprehensive analysis report
│
├── models/
│   ├── classifier.pkl          # Trained model
│   └── vectorizer.pkl          # TF-IDF vectorizer
│
├── src/
│   ├── scraper.py             # Web scraping scripts
│   ├── preprocessor.py        # Text preprocessing
│   ├── train.py               # Model training
│   └── predict.py             # Prediction functions
│
├── app.py                     # Streamlit application
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8 or higher
pip package manager
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sinhala-news-classifier.git
cd sinhala-news-classifier
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## 📈 Model Performance

The Logistic Regression classifier demonstrates strong performance across all news categories, with detailed metrics available in the Jupyter Notebook analysis report.

**Key Metrics:**
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix Analysis
- Category-wise Performance Breakdown

## 🎓 Learning Outcomes

This project provided hands-on experience in:

- **Ethical Web Scraping**: Understanding legal boundaries and responsible data collection
- **Exploratory Data Analysis**: Comprehensive data investigation and visualization
- **NLP for Sinhala**: Text processing challenges in non-English languages
- **ML Pipeline Development**: End-to-end machine learning workflow
- **Model Deployment**: Creating interactive applications for ML models
- **Professional Documentation**: Technical writing and analytical reporting

## ⚖️ Legal & Ethical Disclaimer

**Important Notice:**

This project is developed **strictly for educational purposes** to demonstrate machine learning and data analysis techniques applied to Sinhala-language content.

- ✅ Uses only publicly available content from Hiru News website
- ✅ No access to private, restricted, or paywalled content
- ✅ Data used exclusively for educational and learning purposes
- ❌ Does not redistribute or commercialize any news content
- ❌ Does not claim ownership of any scraped data

**All news text, images, and related materials remain the intellectual property and copyright of Hiru News.**

The project respects:
- Copyright laws and intellectual property rights
- Website terms of service and robots.txt directives
- Ethical web scraping practices
- Data privacy and responsible AI principles

## 🔗 Links

- **Source Code**: [GitHub Repository](https://lnkd.in/gfjCgiQ6)
- **Hiru News**: Original data source (educational use only)

## 🤝 Contributing

This is an educational project. If you're interested in contributing or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is for educational purposes. Please respect the intellectual property rights of Hiru News and use this code responsibly.

## 👨‍💻 Author

Developed as an educational exercise to apply data analysis and machine learning techniques to Sinhala-language news classification.

## 🙏 Acknowledgments

- Hiru News for providing publicly accessible news content
- Open-source community for the amazing tools and libraries
- Educational resources that made this learning journey possible

---

**⚠️ Educational Project Notice**: This project is a learning exercise in machine learning and data analysis. It demonstrates technical skills while maintaining ethical standards and respecting intellectual property rights.

**📧 Questions or Feedback?** Feel free to open an issue or reach out!

---

*Made with ❤️ for learning and education*

