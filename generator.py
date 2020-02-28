
import random
"""demonstrate a generator function. The characteristic is the keyword yield. 
In addition to appending a value to the return collection, it does not terminate the code execution
"""
def lottery( n ):
    # returns n numbers between 1 and 40
    for i in range( n-1 ):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(30, 80)

for ticket in lottery( 5 ):
       print("And the next ticket is... %d!" %(ticket))
