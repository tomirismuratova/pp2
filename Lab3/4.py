import math

class Point:
    def __init__(self, x, y):
        self.x = x    
        self.y = y    

    def show(self):
        print(self.x, self.y)   

    def move(self, new_x, new_y):
        self.x = new_x          
        self.y = new_y          

    def dist(self, point2):
        d = math.sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)
        print(d)   

p1 = Point(2, 3)   
p2 = Point(5, 7)   

p1.show()   
p2.show()   

p1.dist(p2) 

p1.move(10, 10)  
p1.show()        


