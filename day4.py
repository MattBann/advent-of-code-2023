def run():
	task1()
	task2()

def task1():
	s = 0
	with open("inputs/day4.txt", "r") as inp:
		for line in inp:
			card = line.split(":")[1].strip()
			t = card.split("|")
			winners = [x for x in t[0].strip().split(" ") if x != ""]
			nums = [x for x in t[1].strip().split(" ") if x != ""]
			score = 0
			for i in nums:
				if i in winners:
					score += 1 if score == 0 else score
			s += score
	print(s)

from collections import defaultdict

def task2():
	s = 0
	with open("inputs/day4.txt", "r") as inp:
		def default(): return 1
		copies = defaultdict(default)
		for line in inp:
			cardNum = int(line.split(":")[0].split(" ")[-1])
			card = line.split(":")[1].strip()
			t = card.split("|")
			winners = [x for x in t[0].strip().split(" ") if x != ""]
			nums = [x for x in t[1].strip().split(" ") if x != ""]
			score = 1
			s+=1
			for i in nums:
				if i in winners:
					copies[cardNum+score] += copies[cardNum]
					score += 1
					s += copies[cardNum]
			
	print(s)

if __name__=='__main__':
	run()
