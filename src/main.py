from analysis_model import *
from report_model import *
from transcription import *
# Setting up new directory
#
selected_Model = 0

match selected_Model:
    case 0:
        model = analysis_model("/Nagata/model/astrollama-3-8b-chat_summary.Q8_0.gguf")
        while(True):
            # have a conversation
                # look for user input
            user_VoiceInput = sr.Recognizer()
            transcription = transcribe(user_VoiceInput)
            print(transcription)
            user_TextInput = transcription
                # pass to model content
            
                # print response to chat label
        
    case 1:
        model = report_Model("/Nagata/model/astrollama-3-8b-chat_summary.Q8_0.gguf")

def response(content, role):
    response = model.llm.create_chat_completion(
      messages = [
          {"role": "system", "content": f"You are a {role}"},
          {
              "role": "user",
              "content": f"{content}"
          }
      ]
  )