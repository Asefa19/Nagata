
class ModelStore():
    def __init__(self):
        self.modelType = 0 # Chat Model


    def saveModel(self, modelType):
        self.modelType = modelType
        print('Store Model', self.modelType)

        
    def retrieveModel(self):
        print('Retrieve Model', self.modelType)
        return self.modelType