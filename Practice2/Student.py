class Student():

    def __init__(self, name:str, tuition:int, subject:str, grade:int):
        self.name = name
        self.tuition = tuition
        self.subject = subject
        self.grade = grade

    def setName(self, name):
        self.name = name
    
    def setTuition(self, tuition):
        self.tuition = tuition

    def setSubject(self, subject):
        self.subject = subject

    def setGrade(self, grade):
        self.grade = grade
    
    def getName(self):
        return self.name
    
    def getTuition(self):
        return self.tuition
    
    def getSubject(self):
        return self.subject
    
    def getGrade(self):
        return self.grade
    
    def getStatus(self):
        if self.grade > 60:
            return 'Approved'
        else:
            return 'Not Approved'
    
    def printStatus(self):
        print('***********************************')
        print('Name: '+str(self.name))
        print('Tuition: '+str(self.tuition))
        print('Subject: '+str(self.subject))
        print('Grade: '+str(self.grade))
        print('Status: '+self.getStatus())
        print('************************************')


    

    