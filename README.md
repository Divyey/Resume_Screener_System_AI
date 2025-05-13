# Resume Screener System AI 🧠📄

An AI-powered ATS (Applicant Tracking System) built with **Streamlit** and **OpenAI GPT-4o Vision** to analyze resumes (PDF) against job descriptions.

---

## 🚀 Features

- **PDF Resume Analysis**: Converts the first page of a PDF resume to an image for vision processing.
- **Job Description Matching**: 
  - Receive a professional HR-style evaluation of the resume.
  - Get a percentage match score and see which keywords are missing.
- **AI-Powered Insights**: Powered by OpenAI GPT-4o Vision model.
- **Simple Interface**: Streamlit web app for easy upload and analysis.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Divyey/Resume_Screener_System_AI.git
cd Resume_Screener_System_AI
```

### 2. Create and Activate Virtual Environment
```
conda create -p venv python=3.10 -y
conda activate ./venv
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Install Poppler (Required for PDF Conversion)

- **macOS:**
```
brew install poppler
```

- **Windows:**  
Download [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases), extract, and add the `bin` folder to your PATH.

### 5. Set Up Environment Variables

Create a `.env` file in the project root with:
```env
OPENAI_API_KEY = "your_openai_api_key_here"
```
### 6. Run the Application
```bash
streamlit run app.py
```
---

## 📚 Tech Stack

- **AI Model:** OpenAI GPT-4o Vision/GPT-4
- **PDF Processing:** `pdf2image` + Poppler
- **Web Interface:** Streamlit
- **Environment Management:** Conda/Pip

---

## 📌 Notes

- PDF resume is analyzed.
- Requires an OpenAI API key with GPT-4o Vision/GPT-4 access.
- Poppler is required for image conversion from PDF.
- For best results, use clear, text-based PDF resumes.

---

## 🖥️ Example Usage

1. Upload your resume in PDF format.
2. Paste your target job description.
3. Click **"Tell Me About the Resume"** for an HR-style review, or **"Percentage match"** for a match score and missing keywords.

## 📫 Contact

For questions, contact [Divyey](mailto: divyey@gmail.com).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/divyey-arora-58b4a6202) 





