def run():
	task1()
	task2()

cards = {
	"2":0,
	"3":1,
	"4":2,
	"5":3,
	"6":4,
	"7":5,
	"8":6,
	"9":7,
	"T":8,
	"J":9,
	"Q":10,
	"K":11,
	"A":12
}

def scoreHand(hand:str) -> int:
	t = 1
	s = set()
	for i in hand:
		s.add(i)
	if len(s) == 1:
		t = 7
	elif len(s) == 2:
		t = 5
		for i in s:
			if hand.count(i) == 4:
				t = 6
	elif len(s) == 3:
		t = 3
		for i in s:
			if hand.count(i) == 3:
				t = 4
	elif len(s) == 4:
		t = 2
	out = t * 10**10
	for i in range(5):
		out += cards[hand[i]] * 10**(2*(4-i))
	return out


def task1():
	with open("inputs/day7.txt", "r") as inp:
		hands = []
		for line in inp:
			hand, bid = line.strip().split(" ")
			hands.append((hand, int(bid)))		
		hands.sort(key=lambda x : scoreHand(x[0]))
		out = 0
		for i in range(len(hands)):
			out += (i+1) * hands[i][1]
		print(out)

cards2 = {
	"2":1,
	"3":2,
	"4":3,
	"5":4,
	"6":5,
	"7":6,
	"8":7,
	"9":8,
	"T":9,
	"J":0,
	"Q":10,
	"K":11,
	"A":12
}

def scoreHand2(hand:str) -> int:
	t = 1
	s = set()
	js = 0
	for i in hand:
		if i == "J":
			js += 1
		else:
			s.add(i)
	if len(s) == 1 or js == 5:
		t = 7
	elif len(s) == 2:
		t = 5
		for i in s:
			if hand.count(i) == 4 or hand.count(i)+js == 4:
				t = 6
	elif len(s) == 3:
		t = 3
		for i in s:
			if hand.count(i) == 3 or hand.count(i)+js == 3:
				t = 4
	elif len(s) == 4:
		t = 2
	out = t * 10**10
	for i in range(5):
		out += cards2[hand[i]] * 10**(2*(4-i))
	return out

def task2():
	with open("inputs/day7.txt", "r") as inp:
		hands = []
		for line in inp:
			hand, bid = line.strip().split(" ")
			hands.append((hand, int(bid)))		
		hands.sort(key=lambda x : scoreHand2(x[0]))
		out = 0
		for i in range(len(hands)):
			out += (i+1) * hands[i][1]
		print(out)

if __name__=='__main__':
	run()
