class Triangle():
    def __init__(self, a, b,c, height):
        self.a= a
        self.b= b
        self.c= c
        self.height= height

    def area(self):
        return (self.b*self.height)/2

triangle= Triangle(1,5,2,3)
print(triangle.area())
