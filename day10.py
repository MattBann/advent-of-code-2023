def run():
	task1()
	task2()

def task1():
	pipes = []
	start = None
	with open("inputs/day10.txt", "r") as inp:
		i = 0
		for line in inp:
			pipes.append(line)
			if "S" in line:
				start = (line.find("S"), i)
			i += 1
	if pipes[start[1]][start[0]-1] in "-FL":
		node = (start[0]-1, start[1])
	elif pipes[start[1]][start[0]+1] in "-7J":
		node = (start[0]+1, start[1])
	elif pipes[start[1]+1][start[0]] in "|LJ":
		node = (start[0], start[1]+1)
	elif pipes[start[1]-1][start[0]] in "|F7":
		node = (start[0], start[1]-1)
	prev = start
	count = 1
	while True:
		if pipes[node[1]][node[0]] == "|":
			if (node[0],node[1]+1) != prev:
				prev = node
				node = (node[0],node[1]+1)
			else:
				prev = node
				node = (node[0],node[1]-1)
		elif pipes[node[1]][node[0]] == "-":
			if (node[0]+1,node[1]) != prev:
				prev = node
				node = (node[0]+1,node[1])
			else:
				prev = node
				node = (node[0]-1,node[1])
		elif pipes[node[1]][node[0]] == "L":
			if (node[0]+1,node[1]) != prev:
				prev = node
				node = (node[0]+1,node[1])
			else:
				prev = node
				node = (node[0],node[1]-1)
		elif pipes[node[1]][node[0]] == "J":
			if (node[0]-1,node[1]) != prev:
				prev = node
				node = (node[0]-1,node[1])
			else:
				prev = node
				node = (node[0],node[1]-1)
		elif pipes[node[1]][node[0]] == "7":
			if (node[0],node[1]+1) != prev:
				prev = node
				node = (node[0],node[1]+1)
			else:
				prev = node
				node = (node[0]-1,node[1])
		elif pipes[node[1]][node[0]] == "F":
			if (node[0],node[1]+1) != prev:
				prev = node
				node = (node[0],node[1]+1)
			else:
				prev = node
				node = (node[0]+1,node[1])
		elif pipes[node[1]][node[0]] == "S":
			break
		count += 1
	print(count // 2)

from collections import deque

def task2():
	pass

if __name__=='__main__':
	run()
