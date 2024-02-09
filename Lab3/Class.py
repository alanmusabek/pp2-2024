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

# 3 task
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

# 4 task

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

class Bank_account():
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance
        pass
    def deposit(self, amount):
        print("The current balance is: ", self.balance)
        self.balance += amount
        print("The new balance is: ", self.balance)
    def withdraw(self, amount):
        if(amount > self.balance):
            print("Balance is less than the amount")
        else:
            self.balance -= amount
        print("The balance is: ", self.balance)

John = Bank_account("John", 25000)
John.deposit(35000)
John.withdraw(100000)

# task 6
# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Define a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print("List of integers:")
print(numbers)

# Use the filter function to extract prime numbers
prime_numbers = list(filter(is_prime, numbers))
print("\nExtract prime numbers of the said list:")
# Print the extracted prime numbers
print(prime_numbers)