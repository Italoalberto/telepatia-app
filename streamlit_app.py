import streamlit as st
import requests

API_BASE = "https://us-central1-telepatia-app.cloudfunctions.net"

st.title("🩺 Medical Assistant Web App")

option = st.radio("Choose input type:", ["Text", "Audio link"])

if option == "Text":
    user_input = st.text_area("Enter patient consultation text:")
    if st.button("Process Text"):
        resp = requests.post(f"{API_BASE}/extract_medical_info", json={"text": user_input})
        data = resp.json()
        st.subheader("Extracted Medical Info")
        st.json(data)

        resp2 = requests.post(f"{API_BASE}/generate_diagnosis", json=data)
        diagnosis = resp2.json()
        st.subheader("Diagnosis & Recommendations")
        st.write(diagnosis.get("output", ""))

elif option == "Audio link":
    audio_url = st.text_input("Enter audio file link (MP3/WAV):")
    if st.button("Transcribe & Process"):
        resp = requests.post(f"{API_BASE}/transcribe_audio", json={"url": audio_url})
        transcription = resp.json().get("transcription", "")

        resp2 = requests.post(f"{API_BASE}/extract_medical_info", json={"text": transcription})
        extracted = resp2.json()

        resp3 = requests.post(f"{API_BASE}/generate_diagnosis", json=extracted)
        diagnosis = resp3.json()

        st.subheader("Transcription")
        st.write(transcription)

        st.subheader("Extracted Medical Info")
        st.json(extracted)

        st.subheader("Diagnosis & Recommendations")
        st.write(diagnosis.get("output", ""))
