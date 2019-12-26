# Create a class called Shape.
# Define a method in it called what_am_i that prints
# "I am a shape" when called.
# Change your Square and Rectangle classes from the previous challenges to
# inherit from Shape, create Square and Rectangle objects, and call the
# new method on both of them.


class Shape():
    def what_am_i(self):
        print("I am a shape")


        
class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2
    

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size
        

rectangle = Rectangle(2, 4)
square = Square(2)
rectangle.what_am_i()
square.what_am_i()
