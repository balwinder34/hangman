class Square():
    square_list=[]

    def __init__(self,s1):
        self.s1 = s1
        self.square_list.append((self.s1))

    def __repr__ (self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

sq1=Square(4)
sq2=Square(25)
sq3=Square(1000)

print(sq1)
print(sq2)
print(sq3)
