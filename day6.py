def run():
	task1()
	task2()

def task1():
	out = 1
	with open("inputs/day6.txt", "r") as inp:
		times = [int(i) for i in inp.readline().split(":")[1].strip().split(" ") if i != ""]
		distances = [int(i) for i in inp.readline().split(":")[1].strip().split(" ") if i != ""]
		for i in range(len(times)):
			count = 0
			for t in range(times[i]):
				if t * (times[i]-t) > distances[i]:
					count += 1
			out *= count
	print(out)

def task2():
	out = 1
	with open("inputs/day6.txt", "r") as inp:
		time = int("".join([i for i in inp.readline().split(":")[1].strip().split(" ") if i != ""]))
		distance = int("".join([i for i in inp.readline().split(":")[1].strip().split(" ") if i != ""]))
		count = 0
		for t in range(time):
			if t * (time-t) > distance:
				count += 1
		out *= count
	print(out)

if __name__=='__main__':
	run()
