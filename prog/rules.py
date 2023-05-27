import socket
import sys

def isVoyelle(letter):
	if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y'):
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

str = "cosette"

print(str)
print(rules1(str))
print(rules2(rules1(str)))
print(rules3(rules2(rules1(str)), "cosette"))

