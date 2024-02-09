# 1
def convertToOunces(grams):
    ounces = 28.3495231*grams
    return ounces

print(convertToOunces(1000))

# 2

def toCentigrade(Fahrenheit):
    c = (5/9) * (Fahrenheit-32)
    return c

print(toCentigrade(350))

# 3
def solve(numheads, numlegs):
    c = (numheads * 4 - numlegs) / 2
    r = numheads - c
    return c, r

print(solve(35, 94))

#4

#5

#6
def reverseString(string):
    j = 0
    for i in range(0, len(string)):
        if(string[i] == " "):
            print(string[j:i])
            j = i + 1
    # for i in range(1, len(string) + 1):
    #     if(string[-i] == ' '):
    #         print(string[j:-i])
    #         j = -i
    return 0

print(reverseString("We are ready"))