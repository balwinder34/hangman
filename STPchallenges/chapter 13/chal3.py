class Shape():
    def __init__(self, l, w):
        self.lenght= l
        self.width= w

    def what_am_i (self):
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rect= Rectangle(2,4)
squa= Square(4,4)

rect.what_am_i()
squa.what_am_i()
