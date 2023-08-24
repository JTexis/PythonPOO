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
        curplist.append(first4())
        #Adding birth date letters
        curplist.append(second6())
        #Adding gender
        curplist.append(third1())
        #Adding federal entity
        curplist.append(fourth2())
        #Adding consonants
        curplist.append(fifth3())
        #Adding random code
        curplist.append(sixth2())
        curpstr = ''.join(curplist)
        return curpstr