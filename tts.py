from gtts import gTTS
import os
import playsound

def speak_question(question, index):
    filename = f"audio/questions/q{index}.mp3"
    
    tts = gTTS(text=question, lang='en')
    tts.save(filename)

    playsound(filename)