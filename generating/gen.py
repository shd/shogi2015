import random

pieces = []

random.seed(8342)

def initpieces():
    pieces = []
    pieces_init = {"L":2,"N":2,"S":2,"G":2,"K":1,"F":9,"B":1,"R":1}
    for x in pieces_init.keys():
        pieces += [x]*pieces_init[x]
    return pieces

def gen(density):
    res = ""
    occupied = {}
    for s in ["s","g"]:
        musthave = ["K",random.choice(["B","R"])]
	pieces = initpieces()
#	print pieces
	for t in range(density):
#	    print occupied
	    x = 0
	    y = 0
	    promo = ""
	    while 1:
		x = random.randint(1,9)
		y = random.randint(1,9)
		if (x,y) in occupied.keys():
		    continue

		pn = random.randint(1,len(pieces))-1
		if musthave != []:
		    if (pieces[pn] != musthave[0]): continue

		if (pieces[pn] == "L" or pieces[pn] == "F") and ((y == 9 and s == "g") or (y == 1 and s == "s")): continue
		if (pieces[pn] == "N") and ((y >= 8 and s == "g") or (y <= 2 and s == "s")): continue

		if pieces[pn] != "K" and pieces[pn] != "G":
		    promo = random.choice(["","p"])

		nifu = 0
		if (pieces[pn] == "F" and promo == ""):
		    for (x1,y1) in occupied.keys():
			if occupied[(x1,y1)] == "F" and x1==x: nifu = 1
		if nifu: continue

		kingsnear = 0
		if (pieces[pn] == "K"):
		    for (x1,y1) in [(-1,0),(-1,-1),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]:
			if (x+x1,y+y1) in occupied.keys() and occupied[(x+x1,y+y1)][0] == "K": kingsnear = 1
		if kingsnear: continue

		if musthave != [] and (pieces[pn] == musthave[0]): musthave.pop(0)

		break

	    p = pieces.pop(pn)+promo+s
	    occupied[(x,y)] = p
	    res += "\shopiece{"+str(x)+"}{"+str(y)+"}{\\"+p+"}"
    return res

f = open('names.in')
for x in f:
    a = x.split('\n')
    u = a[0].split(';')
    print ("\\testwork{"+u[0]+"}{"+u[1]+"}{"+gen(3)+"}{"+gen(5)+"}")
