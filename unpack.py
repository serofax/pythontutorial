def plus(*args):
    sum = 0;
    for x in args:
        sum += x
    return sum



a = range(20)

print(plus(*range(123)))


