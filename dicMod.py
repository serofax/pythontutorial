dic = {}

def add(key,obj):
    dic[key] = obj

def get(key):
    if key not in dic:
        return None
    else:
        return dic[key]
