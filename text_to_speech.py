# import the pyttsx module inside program
import pyttsx3
w=input()
# initializing the module
engine = pyttsx3.init()

# .say() function is used to speak the text you have written 
# inside the function
engine.say(w)

# this is used to process and run the program commands
engine.runAndWait()
