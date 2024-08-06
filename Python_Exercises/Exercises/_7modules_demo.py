"""
https://docs.python.org/3/library/index.html
"""

import math
from math import sqrt
import _4class_objects as student

class ModulesDemo():

    def builtin_modules(self, number):
        # print(math.factorial(number))
        # print(sqrt(number))
        return math.factorial(number), sqrt(number)

    def student_info(self, name, standard, age):
        student.StudentDetails.__init__(self, name, standard, age)
        student.StudentDetails.display_student_info(self)

m=ModulesDemo()
factorial,square_root=m.builtin_modules(4)
print(f"Factorial: {factorial} Square Root: {square_root}")
m.student_info('Gokul','I',6)