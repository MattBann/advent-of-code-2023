def run():
	task1()
	task2()

def task1():
	out = 0
	with open("inputs/day9.txt", "r") as inp:
		for line in inp:
			vals = [list(map(int, line.split(" ")))]
			i = 0
			while vals[i].count(0) != len(vals[i]):
				vals.append([vals[i][j+1]-vals[i][j] for j in range(len(vals[i])-1)])
				i += 1
			vals[i].append(0)
			while i > 0:
				i -= 1
				vals[i].append(vals[i][-1]+vals[i+1][-1])
			out += vals[0][-1]
	print(out)

def task2():
	out = 0
	with open("inputs/day9.txt", "r") as inp:
		for line in inp:
			vals = [list(map(int, line.split(" ")))]
			i = 0
			while vals[i].count(0) != len(vals[i]):
				vals.append([vals[i][j+1]-vals[i][j] for j in range(len(vals[i])-1)])
				i += 1
			vals[i].insert(0,0)
			while i > 0:
				i -= 1
				vals[i].insert(0,vals[i][0]-vals[i+1][0])
			out += vals[0][0]
	print(out)

if __name__=='__main__':
	run()
