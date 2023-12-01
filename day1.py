def run():
	task1()
	task2()

def task1():
	s = 0
	with open("inputs/day1.txt", "r") as inp:
		for line in inp:
			for i in line:
				if i.isdigit():
					first = i
					break
			for i in line[::-1]:
				if i.isdigit():
					last = i
					break
			s += int(first+last)
	print(s)

def task2():
	words = [
		"zero",
		"one",
		"two",
		"three",
		"four",
		"five",
		"six",
		"seven",
		"eight",
		"nine",
	]
	s = 0
	with open("inputs/day1.txt", "r") as inp:
		for line in inp:
			for i in range(len(line)):
				if line[i].isdigit():
					first = line[i]
					break
				elif i < len(line)-3 and line[i:i+3] in words:
					first = str(words.index(line[i:i+3]))
					break
				elif i < len(line)-4 and line[i:i+4] in words:
					first = str(words.index(line[i:i+4]))
					break
				elif i < len(line)-5 and line[i:i+5] in words:
					first = str(words.index(line[i:i+5]))
					break
			for i in reversed(range(len(line))):
				if line[i].isdigit():
					last = line[i]
					break
				elif i > 1 and line[i-2:i+1] in words:
					last = str(words.index(line[i-2:i+1]))
					break
				elif i > 2 and line[i-3:i+1] in words:
					last = str(words.index(line[i-3:i+1]))
					break
				elif i > 3 and line[i-4:i+1] in words:
					last = str(words.index(line[i-4:i+1]))
					break
			s += int(first+last)
	print(s)

if __name__=='__main__':
	run()
