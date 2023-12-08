def run():
	task1()
	task2()

def task1():
	with open("inputs/day8.txt", "r") as inp:
		instructions = inp.readline().strip()
		inp.readline() # Skip empty line
		nodemap = {}
		for line in inp:
			node, l, r = line.replace(" = ("," ").replace(",","").replace(")","").strip().split(" ")
			nodemap[node] = (l, r)
		
		count = 0
		i = 0
		node = "AAA"
		while node != "ZZZ":
			inst = instructions[i]
			node = nodemap[node][0 if inst=="L" else 1]
			count += 1
			i = (i+1) % len(instructions)
		print(count)

def task2():
	pass
if __name__=='__main__':
	run()
