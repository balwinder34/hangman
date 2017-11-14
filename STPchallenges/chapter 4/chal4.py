x=65

def f():
    global x
    return x/2
"""
    This function takes an integer divides by 2
"""
z= f()

def g(z):
    return z*4
"""
    this function takes the result of the first function and
    multiplies it by 4
"""
print(g(z))
