def run():
	task1()
	task2()

def task1():
	s = 0
	lines = []
	with open("inputs/day3.txt", "r") as inp:
		for line in inp:
			lines.append(line.strip())
	for i in range(len(lines)):
		j = 0
		start = -1
		while j < len(lines[i]):
			if lines[i][j].isdigit() and start == -1:
				start = j
			if (j < len(lines[i])-1 and not lines[i][j+1].isdigit() and start != -1) or (j == len(lines[i])-1 and start!=-1):
				num = int(lines[i][start:j+1])
				valid = False
				if start > 0:
					if lines[i][start-1] != "." and not lines[i][start-1].isdigit():
						valid = True
					elif i > 0 and lines[i-1][start-1] != "." and not lines[i-1][start-1].isdigit():
						valid = True
					elif i < len(lines)-1 and lines[i+1][start-1] != "." and not lines[i+1][start-1].isdigit():
						valid = True
				if not valid and j < len(lines[i])-1:
					if lines[i][j+1] != "." and not lines[i][j+1].isdigit():
						valid = True
					elif i > 0 and lines[i-1][j+1] != "." and not lines[i-1][j+1].isdigit():
						valid = True
					elif i < len(lines)-1 and lines[i+1][j+1] != "." and not lines[i+1][j+1].isdigit():
						valid = True
				if not valid:
					for k in range(start, j+1):
						if i > 0 and lines[i-1][k] != "." and not lines[i-1][k].isdigit():
							valid = True
							break
						if i < len(lines)-1 and lines[i+1][k] != "." and not lines[i+1][k].isdigit():
							valid = True
							break
				if valid:
					s += num
				start = -1
			j += 1
	print(s)

from collections import defaultdict

def task2():
	out = 0
	lines = []
	gears = defaultdict(list)
	with open("inputs/day3.txt", "r") as inp:
		for line in inp:
			lines.append(line.strip())
	for i in range(len(lines)):
		j = 0
		start = -1
		while j < len(lines[i]):
			if lines[i][j].isdigit() and start == -1:
				start = j
			if (j < len(lines[i])-1 and not lines[i][j+1].isdigit() and start != -1) or (j == len(lines[i])-1 and start!=-1):
				num = int(lines[i][start:j+1])
				s = start
				start = -1
				if s > 0:
					if lines[i][s-1] == "*":
						gears[(i, s-1)].append(num)
					elif i > 0 and lines[i-1][s-1] == "*":
						gears[(i-1, s-1)].append(num)
					elif i < len(lines)-1 and lines[i+1][s-1] == "*":
						gears[(i+1, s-1)].append(num)
				if j < len(lines[i])-1:
					if lines[i][j+1] == "*":
						gears[(i, j+1)].append(num)
					elif i > 0 and lines[i-1][j+1] == "*":
						gears[(i-1, j+1)].append(num)
					elif i < len(lines)-1 and lines[i+1][j+1] == "*":
						gears[(i+1, j+1)].append(num)
				for k in range(s, j+1):
					if i > 0 and lines[i-1][k] == "*":
						gears[(i-1, k)].append(num)
					if i < len(lines)-1 and lines[i+1][k] == "*":
						gears[(i+1, k)].append(num)
			j += 1
	print(gears)
	for gear in gears.keys():
		if len(gears[gear]) == 2:
			out += gears[gear][0]*gears[gear][1]
	print(out)

if __name__=='__main__':
	run()
