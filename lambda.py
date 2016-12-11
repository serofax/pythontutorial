def operX(x,operatorFunc):
    return lambda a: operatorFunc(a,x)

plus5 = operX(5,lambda a,b: a+b);
minus5 = operX(5,lambda a,b: a-b);


print(plus5(10))
print(minus5(10))


a = [1,2,3,4,5,6]

