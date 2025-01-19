from pydub import AudioSegment
from pydub.playback import play


# Load the audio file
audio = AudioSegment.from_file("./IsThisLove.mp3")

# Get the first 5 seconds of the audio
first_10_seconds = audio[:10000]  # 5000 milliseconds = 5 seconds

# Play the first 5 seconds
play(first_10_seconds)


# Import the required module for text  
# to speech conversion
import pyttsx3
engine = pyttsx3.init("espeak")  # Or "nsss", "sapi5" if on Windows 
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
   print(voice.id)

engine.say("Hello World")
engine.runAndWait()

engine.say("Hello World")
engine.runAndWait()

 
# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()

engine.say("Hello to you also!")
engine.runAndWait()


# say method on the engine that passing input text to be spoken
engine.say('Hello sir, Hello sir how may I help you?')
 
# run and wait method, it processes the voice commands. 
engine.runAndWait()

# say method on the engine that passing input text to be spoken
engine.say('Why is this not working?')
 
# run and wait method, it processes the voice commands. 
engine.runAndWait()
