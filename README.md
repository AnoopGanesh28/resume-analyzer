# 📄 Resume Analyzer

An AI/ML-powered web application built with **Python, Flask, and NLP techniques**, designed to analyze resumes against job descriptions and provide a similarity score.
This project helps job seekers and recruiters quickly evaluate how well a resume matches a given job posting — a great showcase project for **AI/ML and backend internship portfolios**.

---

## ✨ Key Features

* **Resume–Job Match Scoring** → Uses **TF-IDF + Cosine Similarity** to measure alignment between resumes and job descriptions.
* **Text Extraction** → Parses PDF and DOCX resumes for clean text.
* **Preprocessing Pipeline** → Cleans, tokenizes, and normalizes resume/job text for fair comparison.
* **User-Friendly Web Interface** → Upload resumes and job descriptions through a simple HTML form.
* **Instant Feedback** → Displays a similarity percentage and key matching insights.
* **Extensible Design** → Modular code structure makes it easy to add ML models or new features.

---

## 🛠️ Tech Stack

* **Backend / Web** → Python, Flask
* **ML / NLP** → Scikit-learn (TF-IDF Vectorizer, Cosine Similarity), NLTK / spaCy
* **Frontend** → HTML, CSS, JavaScript
* **File Handling** → pdfplumber, python-docx
* **Environment** → Virtual environment (venv)

---

## 📂 Project Structure

```
RESUME-ANALYZER
│── app.py                 # Main Flask app
│── config.py              # Configurations (paths, constants)
│── requirements.txt       # Dependencies
│── models/
│   └── vectorizer.pkl     # Pre-trained vectorizer
│
│── utils/
│   ├── __init__.py
│   ├── text_extraction.py # PDF/DOCX parsing
│   ├── preprocessing.py   # Text cleaning & tokenization
│   └── similarity.py      # Cosine similarity scoring
│
│── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── uploads/           # Uploaded resumes
│
│── templates/
│   ├── base.html
│   ├── index.html         # Upload form
│   └── result.html        # Show results
│
│── data/
│   ├── resumes/           # Sample resumes
│   └── job_descriptions/  # Sample job descriptions
│
│── logs/
│   └── app.log            # Log files
│
│── tests/                 # Unit tests
│   ├── test_preprocessing.py
│   ├── test_similarity.py
│   └── test_text_extraction.py
│
└── README.md
```

---

## ⚡ Getting Started

### ✅ Prerequisites

* Python 3.x installed
* Virtual environment recommended

### 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

Create and activate a virtual environment:

```bash
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask app:

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000/
```

1. Upload a **resume** (PDF/DOCX).
2. Upload a **job description** (TXT/PDF).
3. View the **similarity score** and analysis on the results page.

---

## 📊 Testing & Validation

Sample data is included in the `data/` folder:

* `data/resumes/` → Example resumes
* `data/job_descriptions/` → Example job postings

Run unit tests:

```bash
pytest tests/
```

---

## 🌱 Roadmap (Future Enhancements)

* Skill extraction and keyword highlighting
* Visualization of matching vs missing skills
* ML-based ranking model for multiple resumes
* Deploy to cloud (Heroku/AWS) for live demo

---

## 👨‍💻 Author

Made with Python, Flask, and perseverance by **Anoop Ganesh** 🚀

---


