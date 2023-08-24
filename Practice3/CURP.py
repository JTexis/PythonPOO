class CURP():

    def __init__(self, name:str, gender:str, birthdate:str, entity:str):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.entity = entity

    def generateCURP(self):
        return 'curp'