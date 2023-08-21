import numpy as np

AlumnsGrades = []
Alumns = {}

average = 0
highest = 0
lowest = 0

option = 0
totalCal = 0

while True:
    print('OPTIONS:')
    print('1) Capture name and grades')
    print('2) Print grades and average')
    print('3) Print grades and lowest grade')
    print('4) Print grades and highest grade')
    print('5) Exit')
    option = input('What option do you want to choose? ')

    if option == '1':
        name = input('Type the alumns name ')
        print('You have type '+str(name))
        numGrades = int(input('How many grades do you desire to capture?: '))
        Grades = [] # List created to storage the grades
        for grade in range(numGrades):
            Grades.append(input('Grade num. '+str(grade+1)+' :'))
        Alumns[name] = Grades

    elif option == '2':
        print(Alumns)
            