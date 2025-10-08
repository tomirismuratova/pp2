class Shape:
    def area(self):
        print(0)   


class Square(Shape):
    def __init__(self, length):
        self.length = length   

    def area(self):
        print(self.length * self.length)   

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  
        self.width = width    
    def area(self):
        print(self.length * self.width)  


s = Shape()
s.area()   

sq = Square(5)
sq.area()  

rect = Rectangle(5, 3)  
rect.area()  
