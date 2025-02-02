import speech_recognition as sr
#import PyAudio

# Init recognizer
def transcribe(self, userVoiceRecognizer):

    while(1):
        try:
    
            with sr.Microphone() as UserVoiceInputSource:
    
                userVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
                print("DJ, come... water...")
                # The Program listens to the user voice input.
                UserVoiceInput = userVoiceRecognizer.listen(UserVoiceInputSource)
    
                UserVoiceInput_converted_to_Text = userVoiceRecognizer.recognize_google(UserVoiceInput)
                UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
                return(UserVoiceInput_converted_to_Text)

        except KeyboardInterrupt:
            print('A KeyboardInterrupt encountered; Terminating the Program !!!')
            exit(0)
        
        except sr.UnknownValueError:
            print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
