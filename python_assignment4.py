# Solution for 1.1
class inputSideTriange:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        s = (self.a + self.b + self.c) // 2
        return s
class areaTriange(inputSideTriange):
    def __init__(self,*args):
        super(areaTriange,self).__init__(*args)
    def area(self,peri):
        self.s = peri
        area = (self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5
        return self.a
a = areaTriange(10,20,30)
p = a.perimeter()
print(p)
print(a.area(p))

# Solution for 1.2
def find_long_words(iterable, thresLength = 1):
    word = list(filter(lambda x: len(x) > thresLength, iterable))
    return word

a = find_long_words(['hello','boy'],4)
print(a)

# Solution for 2.1
def word_len_mapper(iterable):
    length = list(map(lambda x: len(x), iterable))
    return (length)

b = word_len_mapper(['ab','cde','erty'])
print(b)

# Solution for 2.2
def volwelChecker(word):
    vow = ['a','e','i','o','u']
    status = list(filter(lambda x: x not in vow, word))
    if len(status) < 1:
        status = True
    else:
        status = False
    return status

c = volwelChecker('p')
print(c)