# Resume Screener System AI 🧠📄

An AI-powered ATS (Applicant Tracking System) built with **Streamlit**, using the **OpenAI Vision API** to screen resumes (PDF) against job descriptions.

---

## 🚀 Features

- Upload resume in **PDF** format
- Enter a **job description**
- Get:
  - ✅ HR-style resume review
  - 📊 Percentage match with missing keywords
- Powered by **GPT-4o Vision**
- PDF converted to image using `pdf2image` for Vision input

---

## 🛠️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/Divyey/Resume_Screener_System_AI.git
cd Resume_Screener_System_AI

### 2. Create and Activate Virtual Environment

```bash
conda create -p venv python=3.10 -y
conda activate ./venv

### 3. Install Dependencies

```bash
pip install -r requirements.txt

### 4. Install Poppler (Mac)

```bash
brew install poppler

### Environment Variables

Create a .env file in the root folder:

```env
OPENAI_API_KEY=your_openai_api_key_here

### Run the App

```bash
streamlit run app.py