

a =  {
    "name":"vince",
    "adress":{
        "city":"Ingolstadt",
        "zipcode":"85049"
    }
}
import json

j = json.dumps(a)

print (j,type(j))

o = json.loads(j)

print(o,type(o))
