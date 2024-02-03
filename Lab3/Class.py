# 1 task
class upperCase_String:
    def __init__(self) -> None:
        self.string = ""
        pass
    def getString(obj):
        obj.string = input("Enter a string:")
    def printString(obj):
        obj.string = obj.string.upper()
        print(obj.string)

a = upperCase_String()

#a.getString()
#a.printString()

# 2 task

class Shape:
    def __init__(obj) -> None:
        obj.Area = 0
        pass
    def area(obj):
        print(obj.Area)
class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.Area = length * length
        pass
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    def CalculateArea(self):
        self.Area = self.length * self.width

square = Square(5)
square.area()

rectangle = Rectangle(25, 30)
rectangle.CalculateArea()
rectangle.area()