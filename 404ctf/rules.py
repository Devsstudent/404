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


def switch_right(str):
	for elem in range(0, len(str) - 1) :
		if isVoyelle(str[elem]):
			poss = get_next_pos_voyelle(str, elem + 1)
			str[elem], str[poss] = str[poss], str[elem]
	return (str)

def rules1(str):
	return (str[::-1])

def rules2(str):
	if (len(str) % 2 == 0):
		res = str[len(str) / 2:]
		res = res + str[:len(str) / 2]
	else:
		res = str.replace(str[round(len(str)/2) - 1], '')
	return (res)

def rules3(str, original):
	if (isVoyelle(str[2])):
		return (switch_right(str))
	return ("")

str = "drapeau"

print(str + "\n")
print(rules1(str) + "\n")
print(rules2(rules1(str)))
print(rules3(rules2(rules1(str)), "drapeau"))

