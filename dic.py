dic = {}

def add(key,obj):
    dic[key] = obj

def get(key):
    if key not in dic:
        return None
    else:
        return dic[key]


objs = ({"name":"vince","age":26},{"name":"vino","age":23})

for obj in objs:
    add (obj["name"],obj)

print (dic)

print (get("andrea"))
print (get("vince"))


b = list(map(lambda x:(x["name"],x),objs))

print (b)

d = dict(b)
print (d)



