from random import randint
from Point import Point


class Animal:
    'represents an animal'
    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species
    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language
    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))
 


def week2():
    p1 = Point(randint(-1000,1000),randint(-1000,1000))
    #p1.setx(randint(-1000,1000))
    #p1.sety(-25)
    val = p1.get()
    p1.move(y=1000,x=499)
    print('This is my Point')
    print(p1)
    print(id(p1))
    print(p1.x, p1.y)


    p2 = Point(randint(-1000,1000), randint(-1000,1000))
    #p2.setx(-500)
    #p2.sety(1500)
    val = p2.get()
    p2.move(y=-15,x=900)
    print('This is my Point')
    print(p2)
    print(id(p2))
    print(p2.x, p2.y)

    aList = [1,2,3]
    print('This is my list')
    print(aList)

    a = Animal()
    a.setSpecies('dog')
    a.setLanguage('drool')
    a.speak()


from Deck import Deck
d = Deck()
#print(d)
p1 = Point('P1', 5, 5)
p2 = Point('P2', 50, -10)
p3 = p1 + p2
#print(p3)

class MyList(list):
    def helloThere(self):
        return "Hi this is MyList class"


ml = MyList()
ml.helloThere()
ml.append(1)
print(ml)

from Point3D import Point3D

p3 = Point3D('my 3d point', 5, 10, 15)
p4 = Point3D('another 3d point', 10,-25, 100)

p5 = p3 + p4
print(p5)

