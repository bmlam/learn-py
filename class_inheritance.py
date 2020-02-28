#! /usr/bin/python3 
""" """ 
class A:
    
    ca_A = "class attribute of A"
    
    def __init__(self):
        self.ia_A = "instance attribute of A instance"
        
class B(A):
 
    ca_B = "class attribute of B"
    
    def __init__(self):
        super().__init__()
        self.ia_B = "instance attribute of B"  

b = B()

print(b.ia_B)
print(b.ca_B)
print(b.ia_A)
print(b.ca_A)