# -*- coding: utf8 -*-

import random

pieces = []

random.seed(8342)

def initpieces():
    pieces = []
    pieces_init = {"L":2,"N":2,"S":2,"G":2,"K":1,"P":9,"B":1,"R":1}
    for x in pieces_init.keys():
        pieces += [x]*pieces_init[x]
    return pieces

def gen(density,verbal):
    res = ""
    res_s = ""
    res_g = ""
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

		if (pieces[pn] == "L" or pieces[pn] == "P") and ((y == 9 and s == "g") or (y == 1 and s == "s")): continue
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

	    p = pieces.pop(pn)
	    occupied[(x,y)] = p+promo+s
	    if verbal == 0:
		res += "\\shopiece{"+str(x)+"}{"+str(y)+"}{\\"+occupied[(x,y)]+"}"
	    else:
		pp = ""
		if promo:
		    pp = "+"
		pp += p + str(x) + str(y)
		if s == "s":
		    if res_s != "": res_s += ", "
		    res_s += pp
		else:
		    if res_g != "": res_g += ", "
		    res_g += pp
    if verbal == 0:
	return res
    else:
	return [res_s, res_g]

def random_rank():
    rank = ["5 кю", "4 кю", "3 кю", "2 кю", "1 кю", "1 дан", "2 дан", "3 дан", "4 дан", "5 дан"]
    return random.choice(rank)

def shopiecescolor (t,s):
    z = t.split(';')
    res = ""
    for a in z:
        a1 = ''
        promo = ''
        if a[0] == '+':
            a1 = a[1:]
	    promo = 'p'
        else:
	    a1 = a

	col = '-1'
	if a1[1] != '.':
	    col = a1[1]

    	res += "\\shopiece{"+col+"}{"+a1[2]+"}{\\"+a1[0]+promo+s+"}"
    return res

def shopieces (x):
    y = x.split('/')
    return shopiecescolor(y[0],'s') + shopiecescolor(y[1],'g')

def g():
    return shopieces(random.choice(["+P31;R.9/K22;L12;P33;P13","+P31;R.9/L11;K22;P23;P13","+P31;L25;R.9/L11;K22;S23;P13"]))

s = []
f = open('names.in')
for x in f:
    a = x.split('\n')
    u = a[0].split(';')
#   sg = gen(4,0)
    s.append((u[2],"\\testwork{"+u[0]+"}{"+u[1]+"}{"+random_rank()+"}{"+random_rank()+"}{"+
                                             random_rank()+"}{"+random_rank()+"}{"+g()+"}"))

for (x,y) in sorted(s):
    print y