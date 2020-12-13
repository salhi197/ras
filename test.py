# -*- coding: utf8 -*
import pyttsx3
engine = pyttsx3.init()
voice = engine.getProperty('voices')[0] # the french voice
engine.setProperty('voice', voice.id)

engine.say('Je lui ai dit, fait gaffe a ton nez') # perfect

engine.say('Tu as bien mangé?') # it works!!

engine.runAndWait()    
