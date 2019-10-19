import speech_recognition as sr
import pyttsx3
import os
from gtts import gTTS

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)

r=sr.Recognizer()

stats = {
    "petrol" : 50,
    "tankSize": 10,
    "battery" : 3,
    "tyre" : 66,
    "economy" : 40,
}

with sr.Microphone() as source:
    print("Adjusting ambience")
    r.adjust_for_ambient_noise(source)
    
print("Running...")
audio = 0


while True:
    with sr.Microphone() as source: 
        print("listening")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        if  "petrol" in text or "fuel" in text:
            engine.say('The tank is at {0} percentage'.format(stats["petrol"])) 
            engine.say('Expect it to run {0} kilometers'.format(stats["petrol"]*stats["tankSize"]/100*stats["economy"]))
            engine.runAndWait()
            if stats["petrol"] < 20:
                engine.say('Top up soon!')
                engine.runAndWait()
        if "battery" in text:
            if stats["battery"] > 40:
                engine.say('Battery health is looking good')
                engine.runAndWait()
            elif stats["battery"] >15:
                engine.say('Battery is low on charge... ')
                engine.runAndWait()
            else:
                engine.say('Battery is critically low. You might want to check it')
                engine.runAndWait()
            engine.say('It is {0} percent charged'.format(stats["battery"]))
            engine.runAndWait()
        if "tyre" in text or  "pressure" in text or "tire" in text:
            if stats["tyre"] > 80:
                engine.say("Tyre pressures are looking good")
                engine.runAndWait()
            else:
                engine.say("Check your tires, you might need to reflate it.")
                engine.runAndWait()
    except:
        pass