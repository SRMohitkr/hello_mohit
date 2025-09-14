                            #-----Mohit birthday or hello message-----

import time
import pyttsx3
currenttime=time.localtime()
def greet():
    if not currenttime.tm_mday==12:
        engine = pyttsx3.init()
        
        # Get current rate
        rate = engine.getProperty("rate")
        print("Default rate:", rate)   # Just for checking
        
        # Set slower rate (e.g. 150 words per minute)
        engine.setProperty("rate", 120)
        
        # Speak
        engine.say("Hello Mohit,")
        engine.runAndWait()
def wish(): 
    if currenttime.tm_mday==12:
            engine = pyttsx3.init()    
            # Get current rate
            rate = engine.getProperty("rate")
            print("Default rate:", rate)   # Just for checking            
            # Set slower rate (e.g. 150 words per minute)
            engine.setProperty("rate", 120)            
            # Speak
            engine.say("Happy Birthday Mohit")
            engine.runAndWait()
if __name__ == "__main__":
    time.sleep(10)  # wait 5 seconds after desktop loads
    greet()
    time.sleep(2)
    wish()

