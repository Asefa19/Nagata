
class ModelStore():
    #def __init__(self):
        
    def saveModel(self, model, role):
        self.model = model
        self.role = role
        print('Store Model')
        
    def retrieveModel(self):
        print('Retrieve Model')
        return self.model, self.role