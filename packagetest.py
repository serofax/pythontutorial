import rstr
import itertools

def rand():
    while True:
        yield rstr.rstr('Vincet',1)

a = rand()

search = "Vince"

def search(gen,search):
    i = 0
    fullstr = ""
    for x in gen:
        char = search[i]
        if x == char:
            i+=1
        else:
            i = 0
        fullstr += x
        if i >= len(search):
            print (fullstr,len(fullstr))
            break

search(a,"Vincent")


