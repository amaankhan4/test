# Speech to Text Web Application
This is a web application that allows users to transcribe their speech in real-time. The application captures audio from the microphone and converts it into text using speech recognition technology. Users can click a button to start and stop the recording, and the transcribed text is displayed on the screen.

Technologies Used
Python
Streamlit: A Python library for building interactive web applications
SpeechRecognition: A Python library for performing speech recognition
PyAudio: A Python library for audio input and output
Installation
Clone the repository:
```
git clone <repository-url>
```
Navigate to the project directory:
```
cd speech-to-text-web-app
```
Install the required dependencies
```
pip install -r requirements.txt
```
This will install Streamlit, SpeechRecognition, and PyAudio.

Install PocketSphinx (offline speech recognition engine):

**Usage**
Run the application:
```
streamlit run app.py
```
Open the provided URL in your web browser.

Click the "Record" button to start recording your speech.

Speak into the microphone, and your speech will be transcribed in real-time.

Click the "Stop" button to stop the recording.
