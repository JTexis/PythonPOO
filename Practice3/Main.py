from Person import Person
from CURP import CURP
from RFC import RFC 

Persons = []

#Registering person
name = input('Wnter your full name with spaces(eg:Roberto Javier Texis Aburto): ')
birthdate = input('Enter your birthdate(eg:DD/MM/YYYY): ')
gender = input('Enter your sex gender(eg:male): ')
entity = input('Enter your birth entity without spaces(eg:BajaCalifornia): ')


curp = CURP(name, gender, birthdate, entity)
rfc = RFC(name, birthdate)

Persons.append(Person(name, curp.generateCURP(), rfc.generateRFC()))

for persons in Persons:
    print(vars(persons))
