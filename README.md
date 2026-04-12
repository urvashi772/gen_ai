**🎙️ AI Interview Bot**
An end-to-end AI application that automates the mock interview process. 
This system parses a candidate's resume, generates personalized behavioral questions using LLMs, conducts the interview via Voice AI, and provides detailed feedback based on the STAR method.

**🚀 System Architecture & User Flow**
The application follows a 5-step pipeline to simulate a real-world interview environment:

* Resume Parsing (app.py): Extracts text from uploaded PDF resumes using PyPDF2.

* AI Question Generation (question_generator.py): Uses Google Gemini 1.5 Flash to analyze the profile and generate context-aware behavioral questions.

* Voice Synthesis (tts.py): Converts generated text into speech using gTTS (Google Text-to-Speech) and plays it for the user.

* Audio Capture & Transcription (recorder.py & transcriber.py): Records user responses via microphone and transcribes them using OpenAI Whisper (Base model).

* Smart Evaluation (feedback.py): Critiques the transcription against the STAR method, providing a score and improvement tips via GPT-4o-mini.

**🛠️ Tech Stack**

* Frontend: Streamlit
* LLM Models: Google Gemini 1.5 Flash & OpenAI GPT-4o-mini
* Transcription: OpenAI Whisper
* Voice AI: gTTS (Google Text-to-Speech)
* Audio Processing: SpeechRecognition, PyAudio, Playsound
* Language: Python 3.9+

 **⚙️ Installation & Setup**
* 1. Clone the Repo:
     Bashgit clone https://github.com/your-username/ai-voice-interviewer.git
     cd ai-voice-interviewer
* 2. Install Required Packages
    Ensure you have FFmpeg installed on your system (required for Whisper and audio processing).
  Bash:
    pip install -r requirements.txt
* 3. Environment Variables
     Create a .env file in the root directory and add your API keys:
     Code snippetGOOGLE_API_KEY=your_gemini_api_key_here
     OPENAI_API_KEY=your_openai_api_key_here
* 4. Project Directory Structure
     Make sure to create the following folders for audio storage:
     Bash:
       mkdir -p audio/questions audio/answers
     
**📖 Module Overview**

**File**                             **Responsibility**
app.py                               Main Streamlit entry point; handles PDF uploads and UI components.
question_generator.py                Contains logic for Gemini-powered personalized question generation.
tts.py                               Converts text questions to .mp3 and handles audio playback.
recorder.py                          Captures 20-second audio snippets from the candidate's microphone.
transcriber.py                       Loads the Whisper "base" model to convert audio responses to text.
feedback.py                          Evaluates the STAR method, tone, and clarity of the response.
