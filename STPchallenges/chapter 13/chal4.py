class Horse():
    def __init__ (self,name,breed, rider):
        self.name= name
        self.breed= breed
        self.rider= rider

class Rider():
    def __init__(self,name):
        self.name=name

ride = Rider("Red Pollard")
Sea = Horse("Seabiscuit","Thoroughbred", ride)
print(Sea.rider.name)
