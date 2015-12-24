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

#76 66 s78 r68 k48 38 28 s38 p16

def random_rank():
    rank = ["5 кю", "4 кю", "3 кю", "2 кю", "1 кю", "1 дан", "2 дан", "3 дан", "4 дан", "5 дан"]
    return random.choice(rank)

theory = ['Дебют Шикенбиша --- последовательность ходов за белых, итоговая диаграмма после девятого хода',
          'Дебют Шикенбиша --- последовательность ходов за чёрных, итоговая диаграмма после девятого хода',
          'Дебют Санкенбиша (схема Исиды) --- последовательность ходов за чёрных, итоговая диаграмма',
          'Дебют Йокофу --- последовательность ходов, вариант быстрой атаки, итоговая диаграмма',
          'Дебют Йокофу --- последовательность ходов, вариант медленной атаки, итоговая диаграмма, укажите опасный ошибочный ход (ловушку)',
          'Крепость Мино --- ходы для построения, итоговый вид (диаграмма), укажите опасный ошибочный ход',
          'Перечислите правила цумэ-сёги',
          'Поясните пословицу <<Пешка за золотом крепче скалы>>, приведите поясняющий пример',
          'Поясните пословицу <<Высоко прыгающий конь --- добыча для пешки>>, приведите поясняющий пример',
          'Недопустимые ходы пешкой и конём']

def shopieces (x):
    y = x.split('/')
    return shopiecescolor(y[0],'s') + shopiecescolor(y[1],'g')

def problem1dan ():
    return shopieces("+R51;N25;N.9;S.8;S.7;S.6/L11;K32;+B53;P43;P33;P23;B24")

path1 = "q2-testwork/tsume1/"
path3 = "q2-testwork/tsume3/"

s = []
f = open('names.in')
for x in f:
    a = x.split('\n')
    u = a[0].split(';')
    r1 = random.randint(1,21)
    r3 = random.randint(1,21)

    s.append((u[2],"\\testwork{"+u[0]+"}{"+u[1]+"}{"+random.choice(theory)+"}{"+random_rank()+"}{"+random_rank()+"}{"+path1+str(r1)+"}{"+path3+str(r3)+"}{"+problem1dan()+"}"))

for (x,y) in sorted(s):
    print y
