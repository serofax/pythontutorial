

def test(*args):
    print (len(args))
    for x in args:
        if x is None:
            print ("None not allowed")
        else:
            print (x)

test('a','b','c',[1,2,3],None)
