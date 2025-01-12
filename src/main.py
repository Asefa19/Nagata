from analysis_model import *
from report_model import *
from transcription import *
from llama_cpp import Llama
# Setting up new directory
#
class ModelSelection():

    def select():
        selected_Model = 0
        match selected_Model:
            case 0:
                model = analysis_model("/Nagata/model/astrollama-3-8b-chat_summary.Q8_0.gguf")
                role = "Data Analyst for Astronomy"
                
                while(True):
                    user_TextInput = ModelSelection.listen()
                        # pass to model content
                    rsp = ModelSelection.response(user_TextInput, role, model)
                    # send rsp to chat label
                
            case 1:
                model = report_Model("/Nagata/model/astrollama-3-8b-chat_summary.Q8_0.gguf")
                role = "Report writer and critic for Astronomy"
                
                while(True):
                    user_TextInput = ModelSelection.listen()
                    rsp = ModelSelection.response(user_TextInput, role, model)
            

    def response(content, role, model):
        rsp = model.llm.create_chat_completion(
        messages = [
            {"role": "system", "content": f"You are a {role}"},
                {
                "role": "user",
                "content": f"{content}"
                }
            ]
        )
        return rsp
    
    def listen():
        user_VoiceInput = sr.Recognizer()
        transcription = transcribe(user_VoiceInput)
        print(transcription)
        return transcription