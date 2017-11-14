a= input("type a string:")
a= str(a)

try:
    def f(a):
        return float(a)
    print(f(a))
    """
        This function is nestled in a try/except clause to
        correct the input of the user who puts a string of
        letters, instead of a number to be floated
    """
except ValueError:
    print("Wait, shit, put only numbers on this string")
