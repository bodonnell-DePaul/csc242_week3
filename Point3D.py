from Point import Point

class Point3D(Point):

    def __init__(self,name, x,y,z):
        Point.__init__(self,name,x,y)
        self.z = z

    def setz(self, z_value):
        self.z = z_value

    def get(self):
        #temp = Point.get()
        #return (temp.x, temp.y, self.z)
        return (self.x, self.y, self.z)
    
    def move(self, x,y,z):
        Point.move(self,x,y)
        self.z += z

    def __add__(self, anotherPoint):
        p1 = Point.__add__(self, anotherPoint)
        return Point3D(p1.name, p1.x, p1.y, self.z+anotherPoint.z)

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Point3D({},{},{})".format(self.x, self.y, self.z)
    

    