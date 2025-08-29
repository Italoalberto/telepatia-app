# 🩺 Medical Assistant App

AI-powered web application for **medical triage assistance**, built with **OpenAI + Firebase Cloud Functions + Streamlit**.

This project integrates **Generative AI (LLMs)** and **speech-to-text (Whisper)** into a full pipeline:
1. **Prototype in Google Colab** to validate the AI core (symptom extraction + diagnosis).
2. **Production-ready app** with Firebase APIs (Node.js + TypeScript) and Streamlit frontend.

---

## Features
- Text-based medical consultation input.
- Audio support:
  - By link (MP3/WAV).
  - Direct upload (via Google Cloud Storage).
- Automatic transcription with **Whisper**.
- Structured medical information extraction:
  - Symptoms
  - Patient details
  - Consultation reason
- AI-based **diagnosis and recommendations**.

---

## Development Pipeline

### 1) AI Prototype (Google Colab)
The first step was validating the AI logic in [this Jupyter notebook](notebooks/solution_notebook.ipynb):  
- Parse free-text medical consultations.
- Extract structured fields (symptoms, patient info, reason).
- Generate diagnosis + recommendations with LLM.

### 2) Backend (Firebase APIs)
Deployed as **Firebase Cloud Functions** in Node.js/TypeScript:
- `transcribe_audio` → transcribes MP3/WAV into text.
- `extract_medical_info` → parses medical info into JSON.
- `generate_diagnosis` → produces AI-based recommendations.

### 3) Frontend (Streamlit)
Interactive interface in **Streamlit**:
- Option 1: Text input.
- Option 2: Audio file link.
- Option 3: Direct audio upload → automatically stored in GCS and processed.

---

## Tech Stack
- **Python**: Streamlit, Requests, Google Cloud SDK
- **Node.js + TypeScript**: Firebase Functions
- **Streamlit Cloud**: frontend deployment
- **Firebase (Blaze Plan)**: secrets, API hosting, Cloud Storage
- **OpenAI API**: Whisper for transcription, GPT for reasoning

---

## Running locally

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/medical-assistant-app.git
   cd medical-assistant-app

2. Create and activate a virtual environment:
   ```bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate      # Windows

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

4. Configure secrets in .streamlit/secrets.toml:
   ```toml
    [gcp]
    project_id = "your-project-id"
    bucket = "your-bucket-name"

    [gcp_service_account]
    # Paste the JSON content of your service account here

5. Run the app:
   ```bash
    streamlit run streamlit_app.py

## Deployment

APIs deployed with Firebase Cloud Functions.

Frontend deployed on Streamlit Cloud.



