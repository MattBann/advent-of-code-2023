def run():
	task1()
	task2()

def task1():
	s = 0
	with open("inputs/day2.txt", "r") as inp:
		for line in inp:
			gameID, sets = line.split(":")
			valid = True
			for game in sets.split(";"):
				for colour in game.split(","):
					num, c = colour.strip().split(" ")
					if "green" in c and int(num) > 13:
						valid = False
					elif "red" in c and int(num) > 12:
						valid = False
					elif "blue" in c and int(num) > 14:
						valid = False
			if valid:
				s += int(gameID.split(" ")[1])
	print(s)


def task2():
	s = 0
	with open("inputs/day2.txt", "r") as inp:
		for line in inp:
			gameID, sets = line.split(":")
			r, g, b = 0, 0, 0
			for game in sets.split(";"):
				for colour in game.split(","):
					num, c = colour.strip().split(" ")
					if "green" in c:
						g = max(g, int(num))
					elif "red" in c :
						r = max(r, int(num))
					elif "blue" in c:
						b = max(b, int(num))
			s += r * g * b
	print(s)

if __name__=='__main__':
	run()
