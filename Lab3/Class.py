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

# 3 task

class Point():
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        pass
    def show(self):
        print(self.coordinate_x, self.coordinate_y)
    def move(self, coordinate_x, coordinate_y):
        print("Внесенные изменения: ", self.coordinate_x, self.coordinate_y, " -> ")
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        print(".")
    def dist(self, first, second):
        print("Дистанция: ", "(", abs(first.coordinate_x - second.coordinate_x), ",", abs(second.coordinate_y - first.coordinate_y), ")")

first_point = Point(25, -9)
second_point = Point(-5, -3)

first_point.show()
second_point.show()

first_point.dist(first_point, second_point)

second_point.dist(second_point, first_point)