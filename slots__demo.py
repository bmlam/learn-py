""" using the magic __slots__ keyword, we eliminate the existence of __dict__ in a class, that means
we cannot add attributes dynamically to an instance or class
""" 
class S(object):

    __slots__ = ['val']

    def __init__(self, v):
        self.val = v


x = S(42)
print(x.val)

x.new = "not possible"
