
""" demonstrate a use case for decorotor: assuming the the input parameter will
always yield the same return value, the decorator remembers stores the pairs of input parameters
and return values in a hash. 
"""
def memoize(f):
    print( "init hash")
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    print( "calculate return value for %d " % (n) )
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(3))
print(fib(5))

""" output:
init hash
calculate return value for 5
calculate return value for 4
calculate return value for 3
calculate return value for 2
calculate return value for 1
calculate return value for 0
5
2
5
"""