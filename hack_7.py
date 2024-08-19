"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    n = 5
    while n >= 0:
        result.append(n)
        n = n-1
    return result  