from Student import Student
import csv

Students = []


Students.append(Student('Roberto', 1272185, 'POO', 69))
Students.append(Student('Juan', 1272185, 'Maths', 80 ))
Students.append(Student('Alex', 1272348, 'Chemics', 90))
Students.append(Student('Ricardo', 1274895, 'Spanish', 78))
Students.append(Student('Sergio', 1274935, 'Automation', 98))
Students.append(Student('Zen', 1234857, 'Advanced Electronic', 77))

Students.append(Student(str(input('Write your name: ')),
                        int(input('Insert the tuition: ')),
                        str(input('Type the subject: ')),
                        int(input('Type the final grade: '))))

with open('Practice2\Students.csv', 'a', newline='') as file:

    dictKeys = vars(Students[0]).keys()
    listKeys = list(dictKeys)
    writer = csv.DictWriter(file, fieldnames=listKeys)

    for student in Students:
        writer.writerow(vars(student))


