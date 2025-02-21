import analysis_model

class ModelStore():
    def __init__(self):
        self.modelType = 0 # Chat Model


    def saveModel(self, modelType):
        self.modelType = modelType
        print('Store Model')

        
    def retrieveModel(self):
        print('Retrieve Model')
        return self.modelType