import speech_recognition as sr

def record_audio(index):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source, phrase_time_limit=20)

    filename = f"audio/answers/a{index}.wav"

    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
 
    return filename