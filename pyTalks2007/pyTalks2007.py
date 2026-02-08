import pyttsx3

userinput = input("Enter text to convert: ")
engine = pyttsx3.init()
engine.say(userinput)
engine.runAndWait()

# To change the voice, we can run the code from above and pick the voice and 
# language combination that we get from the engine and then 
# set it through the index position in the voices list.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# To change the speed, we can read the `rate` property and 
# set it to a different value than the 200.
rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 100)