def divByZero(n):
    try:
        res = n/0
        return  res
    except Exception as e:
        # print("Number not divisible by zero")
        return e
a = divByZero(5)
print(a)

def sentenceGen():
    subjects = ["Americans ", "Indians"]
    verbs = ["play", "watch"]
    objects = ["Baseball", "Cricket"]
    sent = []
    for s in subjects:
        for v in verbs:
            for o in objects:
                sent.append(s+' '+v+' '+o)
    return sent

b = sentenceGen()
print(b)
