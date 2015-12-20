f = open('names.in')
res = []
for x in f:
    res.append(x.split(';')[0])

print ";".join(res)