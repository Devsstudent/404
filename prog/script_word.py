import socket
import time
import fcntl, os
import errno
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

def get_next_pos_voyelle_r(str, pos):
	i = pos
	while (i > -1):
		if (isVoyelle(str[i])):
			return i
		i = i - 1
	return (len(str) - 1)

def switch_right(st):
	li = list(st)
	i = 0;
	poss = 0
	idx = -1
	while (i < len(st)):
		if isVoyelle(li[i]) and poss == 0:
			idx = i
			poss = get_next_pos_voyelle(li, i + 1)
			if (poss == len(st) - 1):
				return "".join(li)
			buff = li[poss]
			li[poss] = li[idx]
			li[idx] = buff
		elif (isVoyelle(li[i]) and i != poss):
			poss = i
			buff = li[poss]
			li[poss] = li[idx]
			li[idx] = buff
		i = i + 1
	return "".join(li)


def switch_left(st):
	li = list(st)
	i = len(st) - 1
	poss = 0
	idx = -1
	while (i > -1):
		if isVoyelle(li[i]) and poss == 0:
			idx = i
			poss = get_next_pos_voyelle_r(li, i - 1)
			if (poss == len(st) - 1):
				return "".join(li)
			buff = li[poss]
			li[poss] = li[idx]
			li[idx] = buff
		elif (isVoyelle(li[i]) and i != poss):
			poss = i
			buff = li[poss]
			li[poss] = li[idx]
			li[idx] = buff
		i = i - 1
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
	if (len(str) <= 2):
		return (str) 
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

def parse_reply(data):
    posave = data.find("\n", data.find("\n") + 1)
    str = data[ posave + 11:data.find("\n", posave + 1) ]
    idx = 0
    res = ""
    while (idx < len(str) -1 ):
	    pos = str.find(" ", idx)
	    print(str[idx:pos])
	    if (res == ""):
		    res = res + order(rules4(rules3(rules2(rules1(str[idx:pos])), str[idx:pos])))
	    else :
		    res = res + " " + order(rules4(rules3(rules2(rules1(str[idx:pos])), str[idx:pos])))
	    idx = pos + 1
	    if (idx == 0):
		    break
    print(res)
    return (res)


i = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenges.404ctf.fr", 30980))
while True:
    time.sleep(0.2)
    try:
        data = s.recv(4096).decode()
        if not data:
            break
        if (i == 0):
            s.send(("cosette" + "\n").encode("utf8"))
        elif (i == 1):
            s.send(("ettesoc" + "\n").encode("utf8"))
        elif (i == 2):
            s.send(("ttsoc" + "\n").encode("utf8"))
        elif (i == 3):
            s.send(("ottsc" + "\n").encode("utf8"))
        elif (i == 4):
            s.send(("PPtt!15QRUWcos" + "\n").encode("utf8"))
        elif (i == 5):
            s.send((parse_reply(data) + "\n").encode("utf8"))
        print(data)
    except socket.error as e:
        if e.errno == errno.ECONNRESET:
            print("Connection reset by peer")
        else:
            print("Socket error:", e)
        break
    i = i + 1
s.close()
 
