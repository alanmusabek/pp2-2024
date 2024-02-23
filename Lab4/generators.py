N = int(input("Enter the number: "))
a = (i**2 for i in range (1, N + 1))
for i in a:
    print(i)

print()
even = (i for i in range(0, N + 1) if (i % 2 == 0))
for i in even:
    print(i, end=", ")

print()
def divisible(n):
    divisible = (i for i in range(0, n + 1) if(i % 3 == 0 and i % 4 == 0))
    for i in divisible:
        print(i, end=",")

divisible(N)
print()
A = int(input("Enter A: "))
B = int(input("Enter B: "))
squares = (i**2 for i in range(A, B + 1))
for i in squares:
    print(i, end=", ")
print()
c = (i * (-1) for i in range((-1)*(N + 1), 0))
for i in c:
    print(i, end=", ")