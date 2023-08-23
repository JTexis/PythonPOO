class Persona():

    def __init__(self, name:str, RFC:str, CURP:str):
        self.name = name
        self.RFC = RFC
        self.CURP = CURP

    def printData(self):
        print('***********************')
        print('Name: '+self.name)
        print('RFC: '+self.RFC)
        print('CURP: '+self.CURP)

    