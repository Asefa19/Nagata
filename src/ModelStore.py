import analysis_model

class ModelStore():
    def __init__(self):
        self.model = analysis_model.analysis_model("../../model/astrollama-3-8b-chat_summary.i1-Q4_K_M.gguf")
        self.role = "Data Analyst for Astronomy"

    def saveModel(self, model, role):
        self.model = model
        self.role = role
        print('Store Model')
        
    def retrieveModel(self):
        print('Retrieve Model')
        return self.model, self.role