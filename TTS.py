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
engine.setProperty('voice', voices[1].id)
while True:
    engine.say('Hello World')
    engine.runAndWait()
engine.stop()
