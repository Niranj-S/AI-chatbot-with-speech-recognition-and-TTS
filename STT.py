import speech_recognition as sr
import pyttsx3
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
recognizer = sr.Recognizer()


with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source, timeout=5)
try:
    recognized_text = recognizer.recognize_google(audio)
    print("You said: " + recognized_text)
    engine.say(recognized_text)
    engine.runAndWait()
except sr.UnknownValueError:
    print("could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
