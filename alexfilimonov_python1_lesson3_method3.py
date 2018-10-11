import functools
#from functools import reduce
def myfilter(sequence, f):
    return reduce(lambda total, current: total + ([current] if f(current) else []), sequence, [])
myfilter(range(10), lambda x: x%2)