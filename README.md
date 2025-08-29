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

APIs deployed with Firebase Cloud Functions and Frontend deployed on Streamlit Cloud.

## Preview of the App

<img src="https://github.com/user-attachments/assets/ff6cc35f-5694-46fd-9700-09d1ed6a6607" width="400">

## Text Only in the input field

<img width="310" height="430" alt="upload-text1" src="https://github.com/user-attachments/assets/7d0faf6e-cb02-4868-a5f3-f2362bd18d5e" />

## Audio Link in the input field

<table>
  <tr>
    <td valign="top" width="50%">
      <img src="https://github.com/user-attachments/assets/06f95c76-0082-445b-ba52-2256198b7aa8" width="100%" />
    </td>
    <td valign="top" width="50%">
      <img src="https://github.com/user-attachments/assets/091a8e37-b944-4ee5-b327-fc8a03b6ff00" width="100%" />
    </td>
  </tr>
</table>

## Upload Audio in the input field

<table>
  <tr>
    <td valign="top" width="50%">
      <img src="https://github.com/user-attachments/assets/443c04e0-ed0b-466b-a1d3-503b7307863a" width="100%" />
    </td>
    <td valign="top" width="50%">
      <img src="https://github.com/user-attachments/assets/111a6b5b-bfbe-48fd-b069-d95d05695c97" width="100%" />
    </td>
  </tr>
</table>

## License

This project is licensed under the GNU General Public License (GPL).



