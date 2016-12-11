a =  {
    "name": "vincent",
    "age": 26
}

def func(name,age):
    print ("Name",name)
    print ("Age",age)

print (a["name"])
func(**a)