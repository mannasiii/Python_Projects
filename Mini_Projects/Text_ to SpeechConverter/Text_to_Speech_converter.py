import pyttsx3

text_speech = pyttsx3.init()

S1 = "What you want to convert "
Speak = input( "What you want to convert to speech : ")

text_speech.say(Speak)

text_speech.runAndWait()

