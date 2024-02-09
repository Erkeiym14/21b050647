class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, l = 0):
        Shape.__init__(self)
        self.length = 1

    def area(self):
        return pow(self.length, 2)
    
a = Square(int(input()))
print(a.area())
print(Square().area())