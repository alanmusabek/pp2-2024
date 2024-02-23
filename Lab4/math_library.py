import math

def degreeToRadian(degree):
    return degree * (math.pi / 180)

print(degreeToRadian(180))

def areaTrapezoid(height, first_base, second_base):
    return ((first_base + second_base) / 2) * height

print(areaTrapezoid(5, 5, 6))

def areaPolygon(n, length):
    p = n * length
    a = (length) / (2 * math.tan(math.pi/n))
    A = (p*a)/2
    return A

print(areaPolygon(4, 25))

def areaParalleogram(length, height):
    A = length * height
    return A

print(areaParalleogram(5, 6))