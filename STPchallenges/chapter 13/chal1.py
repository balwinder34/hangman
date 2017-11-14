class Rectangle():
    def __init__(self, l, w):
        self.lenght= l
        self.width= w

    def calculate_perimeter(self):
        return 2*(self.lenght+self.width)

class Square():
    def __init__(self,s1):
        self.side1 = s1


    def calculate_perimeter(self):
        return 4*self.side1

rect= Rectangle(2,4)
squa= Square(4)

print(rect.calculate_perimeter())
print(squa.calculate_perimeter())
