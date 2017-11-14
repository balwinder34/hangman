class Square():
    square_list=[]

    def __init__(self,s1):
        self.side1 = s1
        self.square_list.append((self.side1))

sq1=Square(4)
sq2=Square(25)
sq3=Square(1000)

print(Square.square_list)
