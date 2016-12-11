debug = False

def initLog(a,override=False):
    if debug | override:
        print (a)


initLog ('moep',True)

initLog (override=True,a='Hehe')
