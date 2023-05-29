import socket
import sys

def isVoyelle(letter):
	if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y'):
		return (True)
	return (False)

def isMajVoyelle(letter):
	if (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'Y'):
		return (True)
	return (False)

def get_next_pos_voyelle(str, pos):
	for elem in range(pos, len(str) - 1):
		if (isVoyelle(str[elem])):
			return elem
	return (len(str) - 1)


def switch_right(st):
	st = st[::-1]
	li = list(st)
	for elem in range(0, len(li) - 1) :
		if isVoyelle(li[elem]):
			poss = get_next_pos_voyelle(li, elem + 1)
			if (poss == len(st) - 1):
				return "".join(li)[::-1]
			buff = li[poss]
			li[poss] = li[elem]
			li[elem] = buff
	return "".join(li)[::-1]

def switch_left(st):
	li = list(st)
	for elem in range(0, len(li) - 1) :
		if isVoyelle(li[elem]):
			poss = get_next_pos_voyelle(li, elem + 1)
			if (poss == len(st) - 1 and isVoyelle(li[poss]) == False):
				return "".join(li)[::-1]
			buff = li[poss]
			li[poss] = li[elem]
			li[elem] = buff
	return "".join(li)

def rules1(str):
	return (str[::-1])

def rules2(str):
	if (len(str) % 2 == 0):
		res = str[round(len(str) / 2):]
		res = res + str[:round(len(str) / 2)]
	else:
		res = str.replace(str[round(len(str)/2) - 1], '')
	return (res)

def rules3(str, original):
	if (isVoyelle(str[2])):
		return (rules2(rules1(switch_right(original))))
	else:
		return (rules2(rules1(switch_left(original))))

def somme(word, idx):
	res = 0
	n = idx + 1
	while (idx >= 0):
		if (isVoyelle(word[idx]) or isMajVoyelle(word[idx])):
			res = res + ord(word[idx]) * pow(2, n - idx)
		idx = idx - 1
	return (res)

def getVp(vp):
	while (vp >= 65):
		if (isVoyelle(chr(vp)) or isMajVoyelle(chr(vp))):
			return (vp)
		vp = vp - 1
	return (vp)

def get_val(vp, word, n):
	vp = getVp(vp)
	return (((vp + somme(word, n - 1)) % 95) + 32)

def rules4(str):
	li = list(str)
	i = 0
	while (i != len(li)):
		if (not isVoyelle(li[i]) and not isMajVoyelle(li[i]) and li[i].isalpha()):
			#print(li[i])
			li.insert(i + 1, chr(get_val(ord(li[i]), li, i)))
		i = i + 1;
	return ("".join(li))

def order(str):
	dict = {}
	for letter in str:
		if (dict.get(letter, 0) == 0):
			dict.update({letter : 1})
		else :
			dict.update({letter : int(dict.get(letter)) + 1})
	res = ""
	val = dict.values()
	while (len(val) - 1 > 0):
		val = list(dict.values())
		max = 0
		idx_buf = -1;
		for idx in range(0, len(val)):
			if (val[idx] > max):
				max = val[idx]
				idx_buf = idx
			elif (val[idx] == max):
				if (idx_buf != -1 and ord(list(dict.keys())[idx]) < ord(list(dict.keys())[idx_buf])):
					idx_buf = idx
					max = val[idx]
		i = 0
		while (i < max) :
			res = res + list(dict.keys())[idx_buf]
			i = i + 1
		if (idx_buf != -1):
			dict.pop(list(dict.keys())[idx_buf])
	return (res)


str = "lecteur doute devine madeleine autre valjean avons regarde profondeurs cette conscience moment regarder encore faisons emotion tremblement existe terrifiant cette sorte contemplation esprit trouver nulle eblouissements tenebres homme fixer aucune chose redoutable compliquee mysterieuse infinie spectacle grand spectacle grand interieur faire poeme conscience humaine propos homme propos infime hommes serait fondre toutes epopees epopee superieure definitive conscience chaos chimeres convoitises tentatives fournaise reves antre idees honte pandemonium sophismes champ bataille passions certaines heures penetrez travers livide humain reflechit regardez derriere regardez cette regardez cette obscurite silence exterieur combats geants comme homere melees dragons hydres nuees fantomes comme milton spirales visionnaires"
idx = 0
res = ""
while (idx < len(str) -1 ):
	pos = str.find(" ", idx)
	if (res == ""):
		res = res + order(rules4(rules3(rules2(rules1(str[idx:pos])), str[idx:pos])))
	else :
		res = res + " " + order(rules4(rules3(rules2(rules1(str[idx:pos])), str[idx:pos])))
	idx = pos + 1
	if (idx == 0):
		break

#print(res)
print(order(rules4(rules3(rules2(rules1("cosette")),"cosette"))))
	
