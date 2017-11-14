class Square():
    def __init__(self,s1):
        self.side1 = s1


    def print_size (self):
        print ("""I am {} by {}""".format(self.side1,self.side1))

    def change_size(self, n):
        self.side1 += n
#the += is the same as typing out addition of self.side1+n
squa= Square(4)
squa.change_size(12)
squa.print_size()
