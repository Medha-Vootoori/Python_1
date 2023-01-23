# import the pyttsx module inside program
import pyttsx3
print("Enter the text :")
w=input()
# initializing the module
in_put = pyttsx3.init()

# .say() function is used to speak the text you have written 
# inside the function
in_put.say(w)

# this is used to process and run the program commands
in_put.runAndWait()
