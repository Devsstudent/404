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
		if (isVoyelle(word[idx])):
			res = res + ord(word[idx]) * pow(2, n - idx)
		idx = idx - 1
	return (res)

def getVp(vp):
	while (vp >= 65):
		if (isVoyelle(chr(vp))):
			return (vp)
		vp = vp - 1

def get_val(vp, word, idx):
	vp = getVp(vp)
	return (((vp + somme(word, idx - 1)) % 95) + 32)

def rules4(str):
	li = list(str)
	i = 0
	while (i != len(li)):
		if (not isVoyelle(li[i]) and not isMajVoyelle(li[i]) and li[i].isalpha()):
			li.insert(i + 1, chr(get_val(ord(li[i]) - 1, li, i)))
		i = i + 1;
	return ("".join(li))

str = "cosette"

print(str)
print(rules1(str))
print(rules2(rules1(str)))
print(rules3(rules2(rules1(str)), "cosette"))
print(rules4("futur"));

