import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'gmw/en-us')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
engine.say("Hello Comp 151, let's talk.")
engine.runAndWait()