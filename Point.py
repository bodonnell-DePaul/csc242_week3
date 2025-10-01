class Point:
    'A simple class representing a 2D point in space'

    def __init__(self,name, xcord=0, ycord=0):
        self.name = name
        self.x=xcord
        self.y=ycord

    def setx(self, value):
        "sets the x value"
        self.x = value
        pass

    def sety(self,value):
        'sets the y value'
        self.y = value

    def get(self):
        'returns a tuple of the values of Point'
        return (self.x, self.y)
    
    def move(self,x,y):
        'Adds the x and y value to the parameters'
        self.x += x
        self.y +=y

    def __add__(self, anotherPoint):
        return Point(self.name, self.x+anotherPoint.x, self.y+anotherPoint.y)
    
    def __sub__(self,anotherPoint):
        return Point(self.name, self.x-anotherPoint.x, self.y-anotherPoint.y)
    
    def __mul__(self, anotherPoint):
        return Point(self.name, self.x*anotherPoint.x, self.y*anotherPoint.y)
    
    def __truediv__(self,anotherPoint):
        return Point(self.name, round(self.x/anotherPoint.x), round(self.y/anotherPoint.y))
    
    def __floordiv__(self,anotherPoint):
        return Point(self.name, self.x//anotherPoint.x, self.y//anotherPoint.y)

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __ne__(self, value):
        return self.x != value.x or self.y != value.y
    
    def __gt__(self, anotherPoint):
        return self.x > anotherPoint.x and self.y > anotherPoint.y

    def __ge__(self, anotherPoint):
        return self.x >= anotherPoint.x or self.y >= anotherPoint.y

    def __lt__(self, anotherPoint):
        return self.x < anotherPoint.x and self.y < anotherPoint.y

    def __le__(self, anotherPoint):
        return self.x <= anotherPoint.x or self.y <= anotherPoint.y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)