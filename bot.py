# setting up aiml
import aiml
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
# setting up pyttsx(talking)
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("hello, pleased to meet u")
engine.runAndWait()
while True:
	input = raw_input("Enter your message >> ")
	output = kernel.respond(input)
	print output
	engine.say(output)
	engine.runAndWait()

