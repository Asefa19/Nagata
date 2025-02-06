from analysis_model import analysis_model
from report_model import report_model
from transcription import transcription
from llama_cpp import Llama
# Setting up new directory
#
class ModelSelection():
    selected = 0
    def select(self, selected_Model):
        # selected_Model = 0
        match selected_Model:
            # Case 0 = analysis model
            case 0:
                model = analysis_model(self, "../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf")
                role = "Data Analyst for Astronomy"
                return model, role
            # Case 1 = report model
            case 1:
                model = report_Model(self, "../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf")
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