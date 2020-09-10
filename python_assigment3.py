# Assignment 3
# Solution to question 1.1
def myReduce(func, iterable, init = None):
    iterator = iter(iterable)
    if init == None:
        value = next(iterator)
    else:
        value = init
    for i in iterator:
        value = func(value,i)
    return value
a = myReduce(lambda x,y: x+y, [1,2,3])
print(a)

# Solution to question 1.2
def myFilter(func,iter):
    temp=[]
    for i in iter :
        if func(i):
            temp.append(i)
    return temp

def isEven(lst):
    if lst % 2 == 0:
        return True
    else:
        return False
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myFilter(isEven, list1))

# Solution to question 2.1
print(['x'*i for i in range(1,5)] + ['y'*i for i in range(1,5)] + ['z'*i for i in range(1,5)])

# Solution to question 2.2
print([['x'*i, 'y'*i, 'z'*i][j] for i in range(1,5) for j in range(3)])

# Solution to question 2.3 (unable to do)
temp = []
for j in range(2,5):
    temp = temp+[[i] for i in range(j, j+3)]
print(temp)

# Solution to question 2.4

k = 2
p = []
for j in range(6,10):
    l = []
    for i in range(k,j):
        l.append(i)
    if len(l) == 4:
        p.append(l)
    k = k + 1
    j = j + 1
print(p)

# Solution to question 2.5
print([(j,i) for i in range(1,4) for j in range(1,4)])




