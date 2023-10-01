import streamlit as st
from pydub import AudioSegment
import speech_recognition as sr
import pandas as pd

st.title("Audio Transcriber")
st.write("By AI খুড়ো")
def main():
    st.write("Upload an audio file to generate a text transcript.")
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

    if uploaded_file:
        st.audio(uploaded_file, format="audio/mp3")
        # Convert uploaded audio to text
        def audio_to_text(uploaded_file):
            audio = AudioSegment.from_file(uploaded_file)
            audio.export("temp.wav", format="wav")
            r = sr.Recognizer()
            with sr.AudioFile("temp.wav") as source:
                audio_data = r.record(source)
                text = r.recognize_google(audio_data)
            return text
        text = audio_to_text(uploaded_file)
        # Display the text transcript
        st.subheader("Transcript:")
        st.write(text)
if __name__ == "__main__":
    main()

