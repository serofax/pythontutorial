
l = list(range(10))

print (l)
l.extend(list(range(20)))

print (l,len(l))

s = set(l)

print (s,len(s))

v = set(range(10)) & set(range(5,15))
c = set(range(10)) | set(range(5,15))
s = set(range(10)) ^ set(range(5,15))

print(v,len(v))
print(c,len(c))
print(s,len(s))
