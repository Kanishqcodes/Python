# In this problem we will import modules and test it! 
# For this one I am importing pyttsx module which converts text to speech 
import pyttsx3

engine = pyttsx3.init()
engine.say("I am Kanishq Panchal")
engine.runAndWait()

# We can also use below line instead of above code to speak
pyttsx3.speak("I am 21 years old")