class MyFirstClass(object):
    """docstring for MyFirstClass"""

    def __init__(self):
        self.numbers = [1,2,3]

    def addNumber(self,number):
        self.numbers.append(number)

    def square(self):
        return list(map(lambda x: x**2,self.numbers))


obj = MyFirstClass()

print (obj)
print (type(obj))
print (obj.square())

for x in range(4,20):
    obj.addNumber(x)

print (obj.square())

