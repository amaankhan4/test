import speech_recognition as sr
import pyaudio
import streamlit as st
def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            return r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return "Error; {0}".format(e)  
