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

def gcd(a, b):
   while(b):
       a, b = b, a % b
   return a

# This function computes LCM
def lcm(a, b):
   lcm = (a*b)//gcd(a,b)
   return lcm

def task2():
	with open("inputs/day8.txt", "r") as inp:
		instructions = inp.readline().strip()
		inp.readline() # Skip empty line
		nodemap = {}
		starts = []
		for line in inp:
			node, l, r = line.replace(" = ("," ").replace(",","").replace(")","").strip().split(" ")
			nodemap[node] = (l, r)
			if node[2] == "A":
				starts.append(node)
		times = []
		for start in starts:
			i = 0
			count = 0
			node = start
			while node[2] != "Z":
				inst = 0 if instructions[i]=="L" else 1
				node = nodemap[node][inst]
				count += 1
				i = (i+1) % len(instructions)
			times.append(count)
		out = times[0]
		for i in range(1, len(times)):
			out = lcm(out, times[i])
		print(out)

if __name__=='__main__':
	run()
