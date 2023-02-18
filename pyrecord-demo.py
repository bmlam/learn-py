"""
pyrecord seems to be not in python3 
"""
from pyrecord import Record 

Student = Record.create_type( "name", 'age', 'attendClass' )

student1 = Student( "John", 13, "math")

print( student1 )

student1.attendClass = 'bio'

print( student1 )