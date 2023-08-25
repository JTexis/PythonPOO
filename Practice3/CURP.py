from utils import *

class CURP():

    def __init__(self, name:str, gender:str, birthdate:str, entity:str):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.entity = entity

    def generateCURP(self):
        curplist = []
        #First 4 letters
        curplist.append(first4(self.name))
        #Adding birth date letters
        curplist.append(second6(self.birthdate))
        #Adding gender
        curplist.append(third1(self.gender))
        #Adding federal entity
        curplist.append(fourth2(self.entity))
        #Adding consonants
        curplist.append(fifth3(self.name))
        #Adding random code
        curplist.append(sixth2())
        curpstr = ''.join(curplist)
        return curpstr