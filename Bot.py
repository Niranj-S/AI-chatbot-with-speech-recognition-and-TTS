import speech_recognition as sr
import google.generativeai as genai

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
    prompt = recognized_text
    genai.configure(api_key="AIzaSyAStFRUod6oIkU5EC9wKEYTJM31r-yDomU")

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2000,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    convo.send_message(prompt)

    ai = convo.last.text
    print(ai)
    engine.say(ai)
    engine.runAndWait()

except sr.UnknownValueError:
    print("could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")



