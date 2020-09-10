# Python assignment 1
# Answer to question 1
def number():
    temp = []
    for i in range(2000,3201,1):
        if i % 7 == 0 and i % 5 != 0:
            temp.append(i)
    return temp
a = number()
print(a)

# Answer to question 2
def revString():
    firstName = input('Please enter first name: ')
    lastName = input('Please enter last name ')
    revName = firstName[::-1]+ ' ' + lastName[::-1]
    return revName
b = revString()
print(b)

# Answer to question 3
import math
def vol(radius):
    vol = (4/3) * math.pi * radius ** 3
    return vol
c = vol(12)
print(c)

# Python assignment 2
# Solution for question 1
def patternMaker():
    for i in range(6):
        print('*'*i)
        if i == 5:
            for i in range(4,0,-1):
                print('*'*i)

a = patternMaker()
a

# Solution for question 2

def strReverse():
    name = input('Enter name ')
    return name[::-1]

b = strReverse()
print(b)