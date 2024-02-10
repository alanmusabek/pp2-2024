from itertools import permutations
import random
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
def print_permutations(string):
    perms = permutations(string)

    for perm in perms:
        print(''.join(perm))

print_permutations("abc")

#6
def reverse_sentence(sentence):
    words = sentence.split()

    reversed_words = words[::-1]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

print(reverse_sentence("We are ready"))

#7
def has_33(nums):
    previous_num = 0
    i = 1
    for item in nums:
        if(item == 3):
            if(previous_num == 3):
                return True
            else:
                previous_num = item
            i += 1
        else:
            previous_num = item
            i += 1
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8

def spy_game(nums):
    previous_num_1 = 0
    previous_num_2 = 0
    i = 1
    for item in nums:
        if(item == 7 and i >= 3):
            if(previous_num_2 == 0):
                if(previous_num_1 == 0):
                    return True
            else:
                previous_num_2 = item
                previous_num_1 = previous_num_2
            i += 1
        else:
            previous_num_2 = item
            previous_num_1 = previous_num_2
            i += 1
    return False
print("SPY GAME")
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
#9
def sphere(radius):
    return 4/3 * (3.14) * pow(radius, 3)

print(sphere(350))

#10
def uniqueList(list):
    unique_elemets = {

    }
    unique_list = []
    for item in list:
        unique_elemets[item] = 0
    for item in list:
        unique_elemets[item] += 1
    for item in list:
        if(unique_elemets[item] == 1):
            unique_list.append(item)
    return unique_list

print(uniqueList([1, 1, 1, 2, 3, 4, 4, 2, 3, 5, 10, 11, 2]))

# 11
def is_palindrome(word):
    word_length = len(word)
    if word_length % 2 == 0:
        first_half = word[:word_length // 2]
        second_half = word[word_length // 2:]
    else:
        first_half = word[:word_length // 2]
        second_half = word[word_length // 2 + 1:]

    return first_half == second_half[::-1]

print(is_palindrome("barnabas"))

#12
def histogram(list):
    for item in list:
        i = item
        while(i > 1):
            print("*", end="")
            i -= 1
        print("*")

histogram([4, 9, 7])

#13
def guess_the_number():
    print("What is your name?")
    name = input()
    print("Well,", name, ", I am thinking of a number between 1 and 20.")
    print("Take a guess")
    guess = int(input())
    real_number = random.randint(1, 20)
    i = 1
    while(real_number != guess):
        if(guess > real_number):
            print("Your guess is too high")
            print("Take a guess")
            guess = int(input())
            i += 1
        elif(guess < real_number):
            print("Your guess is too low")
            print("Take a guess")
            guess = int(input())
            i += 1
    if(guess == real_number):
        string = "Good job, {}! You guessed my number in {} guesses!"
        print(string.format(name, i))
#guess_the_number()

