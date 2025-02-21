from analysis_model import analysis_model
from report_model import report_model
from transcription import transcribe
from llama_cpp import Llama
import speech_recognition as sr
import ModelStore
from utils import clean_text


class ModelSelection():
    selected = 0
    def __init__(self):
        self.modelType = 0
        self.user_textInput=""
        #self.model_store = ModelStore()
        
    # def select(self, selected_Model):
    #     # selected_Model = 0
    #     match selected_Model:
    #         # Case 0 = analysis model
    #         case 0:
    #             # Chat Model (0)
    #             modelType = 0            
    #         # Case 1 = report model
    #         case 1:
    #             # Research Model (1)
    #             modelType = 1 
    #     return ModelStore.saveModel(modelType)

    # def response(self, textInput):
    #     self.user_textInput = textInput
    #     #user_TextInput = ModelSelection.listen()        
    #     model, role = self.modelInfo.retrieveModel()

    #     rsp = model.create_chat_completion(
    #     messages = [
    #         {"role": "system", "content": f"You are a {role}"},
    #             {
    #             "role": "user",
    #             "content": f"{self.user_textInput}"
    #             }
    #         ]
    #     )
    #     #rsp = clean_text(rsp)
    #     return rsp
    
    # def listen(self):
    #     user_VoiceInput = sr.Recognizer()
    #     transcription = transcribe(user_VoiceInput)
    #     print(transcription)
    #     return transcription