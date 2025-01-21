from analysis_model import *
from report_model import *
from transcription import *
from llama_cpp import Llama
# Setting up new directory
#
class ModelSelection():

    def select(self, selected_Model):
        # selected_Model = 0
        match selected_Model:
            # Case 0 = analysis model
            case 0:
                model = analysis_model("/Nagata/model/astrollama-3-8b-chat_summary.Q8_0.gguf")
                role = "Data Analyst for Astronomy"
                return model, role
            # Case 1 = report model
            case 1:
                model = report_Model("/Nagata/model/astrollama-3-8b-chat_summary.Q8_0.gguf")
                role = "Report writer and critic for Astronomy"
                return model, role


    def response(self, role, model):
        user_TextInput = ModelSelection.listen()
        rsp = model.llm.create_chat_completion(
        messages = [
            {"role": "system", "content": f"You are a {role}"},
                {
                "role": "user",
                "content": f"{user_TextInput}"
                }
            ]
        )
        return rsp
    
    def listen(self):
        user_VoiceInput = sr.Recognizer()
        transcription = transcribe(user_VoiceInput)
        print(transcription)
        return transcription