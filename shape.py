#Define a class named Shape and its subclass Square. The Square class has an init function which
#takes length as argument. Both classes have an area function which can print the area of the shape
#where Shape’s area is 0 by default.
class Shape():
    area=0
   
    def ar(self):
        
       
        print("area of the shape is  \n  ",self.area)

class Square(Shape):
    
    def __init__(self,length):
        self.length=length

    def ar(self):
        print("area of the shape is \n  ",Shape.area)
a1=Shape()
b1=Square(1)
a1.ar()
b1.ar()
