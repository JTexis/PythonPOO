class Person():

    def __init__(self, name:str, CURP:str=None, RFC:str=None):
        self.name = name
        self.RFC = RFC
        self.CURP = CURP

    def printData(self):
        print('***********************')
        print('Name: '+self.name)
        print('RFC: '+self.RFC)
        print('CURP: '+self.CURP)

    