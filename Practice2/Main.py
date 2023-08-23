from Student import Student


Students = []

Students.append(Student('Roberto', 1272185, 'POO', 69))
Students.append(Student('Juan', 1272185, 'Maths', 80 ))
Students.append(Student('Alex', 1272348, 'Chemics', 90))
Students.append(Student('Ricardo', 1274895, 'Spanish', 78))
Students.append(Student('Sergio', 1274935, 'Automation', 98))
Students.append(Student('Zen', 1234857, 'Advanced Electronic', 77))

for student in Students:
    student.printStatus()