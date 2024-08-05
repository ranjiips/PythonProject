"""
Object Oriented Programming
"""


class StudentDetails(object):
    # school = 'Universal Public School'

    def __init__(self, name, standard, age):
        self.name = name
        self.standard = standard
        self.age = age
        self.school='Universal Public School'

    def display_student_info(self):
        print("Display Student Details from Parent class")
        print("Student Name: {}, Class: {}".format(self.name, self.standard))
        print("Student Age: {}".format(self.age))
        print("School: {}".format(self.school))
        print('*'*40)

stud = StudentDetails('Gokul','IV',8)
stud.school='Nandhini'
print(stud.display_student_info())
stud = StudentDetails('Ajay', 'V',9)
print(stud.display_student_info())
print("School: {}".format(stud.school))
print(stud.name)
print(stud.standard)