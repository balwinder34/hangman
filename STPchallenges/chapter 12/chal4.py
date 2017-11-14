class Hexagon():
    def __init__(self, s):
        self.side= s

    def perimeter(self):
        return 6*self.side

hex= Hexagon(35)
print(hex.perimeter())
