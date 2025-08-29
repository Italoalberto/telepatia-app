import streamlit as st
import requests
from google.cloud import storage
from datetime import timedelta
from uuid import uuid4
from pathlib import Path
import mimetypes

API_BASE = "https://us-central1-telepatia-app.cloudfunctions.net"

st.title("🩺 Medical Assistant Web App")

# ---------- helpers ----------
def call_extract(text: str):
    return requests.post(f"{API_BASE}/extract_medical_info", json={"text": text}).json()

def call_generate(extracted: dict):
    return requests.post(f"{API_BASE}/generate_diagnosis", json=extracted).json()

def call_transcribe(url: str):
    return requests.post(f"{API_BASE}/transcribe_audio", json={"url": url}).json()

def upload_to_gcs(file) -> str:
    """
    Sobe o arquivo para o bucket e retorna uma URL ASSINADA (GET, expira em 1h).
    Mantém o bucket privado.
    """
    client = storage.Client.from_service_account_info(st.secrets["gcp_service_account"])
    bucket = client.bucket(st.secrets["gcs_bucket"])

    # Nome do objeto
    ext = Path(file.name).suffix or mimetypes.guess_extension(file.type) or ".mp3"
    blob = bucket.blob(f"uploads/{uuid4()}{ext}")

    # Upload
    blob.upload_from_file(file, content_type=file.type or "audio/mpeg")

    # URL assinada (mais seguro que tornar o objeto público)
    signed_url = blob.generate_signed_url(expiration=timedelta(hours=1), method="GET")
    return signed_url

def pipeline_from_text(text: str):
    with st.spinner("Extraindo entidades médicas..."):
        extracted = call_extract(text)
    with st.spinner("Gerando diagnóstico e recomendações..."):
        diagnosis = call_generate(extracted)

    st.subheader("Extracted Medical Info")
    st.json(extracted)
    st.subheader("Diagnosis & Recommendations")
    st.write(diagnosis.get("output", ""))

def pipeline_from_audio_url(audio_url: str):
    with st.spinner("Transcrevendo áudio..."):
        tr = call_transcribe(audio_url)
        transcription = tr.get("transcription", "")
    st.subheader("Transcription")
    st.write(transcription or "_(vazio)_")

    if transcription:
        pipeline_from_text(transcription)

# ---------- UI ----------
option = st.radio("Choose input type:", ["Text", "Audio link", "Upload audio"])

if option == "Text":
    user_input = st.text_area("Enter patient consultation text:")
    if st.button("Process Text") and user_input.strip():
        pipeline_from_text(user_input.strip())

elif option == "Audio link":
    audio_url = st.text_input("Enter audio file link (MP3/WAV):")
    if st.button("Transcribe & Process") and audio_url.strip():
        try:
            pipeline_from_audio_url(audio_url.strip())
        except Exception as e:
            st.error(f"Erro ao processar o áudio: {e}")

elif option == "Upload audio":
    file = st.file_uploader("Send an audio file (MP3/WAV)", type=["mp3", "wav"])
    if st.button("Upload, Transcribe & Process") and file is not None:
        try:
            with st.spinner("Enviando para o Storage..."):
                signed_url = upload_to_gcs(file)
            st.success("Upload concluído!")
            st.caption("Usando URL assinada (expira em 1h).")
            st.write(signed_url)

            pipeline_from_audio_url(signed_url)
        except Exception as e:
            st.error(f"Falha no upload ou transcrição: {e}")
