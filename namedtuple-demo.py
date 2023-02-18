
from collections import namedtuple 

Student = namedtuple( "Student", ["name", 'age', 'attendClass'] )

student1 = Student( "John", 13, "math")

print( student1 )

""""
wont work: student1.attendClass = 'bio'
"""
student1 = student1._replace( attendClass = "bio")

print( student1 )