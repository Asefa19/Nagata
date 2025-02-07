from analysis_model import analysis_model
from report_model import report_model
from transcription import transcribe
from llama_cpp import Llama
import speech_recognition as sr
import ModelStore

# Setting up new directory

class ModelSelection():
    selected = 0
    def __init__(self):
        self.modelInfo = ModelStore.ModelStore()
        self.user_textInput=""
        
    def select(self, selected_Model):
        # selected_Model = 0
        match selected_Model:
            # Case 0 = analysis model
            case 0:
                # model = analysis_model(self, "../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf")
                model = analysis_model(self, "../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf")
                role = "Data Analyst for Astronomy"
                self.modelInfo.saveModel(model, role)                
            # Case 1 = report model
            case 1:
                # model = report_model(self, "../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf")
                model = report_model(self, "../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf")
                role = "Report writer and critic for Astronomy"
                self.modelInfo.saveModel(model, role)    

    def response(self, textInput):
        self.user_textInput = textInput
        #user_TextInput = ModelSelection.listen()        
        model, role = self.modelInfo.retrieveModel()
        
        rsp = model.llm.create_chat_completion(
        messages = [
            {"role": "system", "content": f"You are a {role}"},
                {
                "role": "user",
                "content": f"{self.user_textInput}"
                }
            ]
        )
        return rsp
    
    def listen(self):
        user_VoiceInput = sr.Recognizer()
        transcription = transcribe(user_VoiceInput)
        print(transcription)
        return transcription