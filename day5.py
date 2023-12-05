def run():
	task1()
	task2()

def task1():
	with open("inputs/day5.txt", "r") as inp:
		seeds = sorted(list(map(int, inp.readline().split(":")[1].strip().split(" "))))
		for _ in range(7):
			inp.readline() # Skip empty line
			inp.readline() # Skip descriptor line
			mapped = []
			while True:
				line = inp.readline()
				if line.strip() == "":
					break
				destStart, srcStart, rng = map(int, line.split(" "))
				i = 0
				while i < len(seeds):
					if seeds[i] >= srcStart and seeds[i] < srcStart+rng:
						mapped.append(seeds[i]+(destStart-srcStart))
						seeds.remove(seeds[i])
					else:
						i += 1
			for i in seeds:
				mapped.append(i)
			seeds = mapped
		print(min(seeds))

def task2():
	with open("inputs/day5.txt", "r") as inp:
		seeds = []
		line = list(map(int, inp.readline().split(":")[1].strip().split(" ")))
		for i in range(len(line)):
			if i % 2 == 1:
				seeds.append((line[i-1], line[i]))
		# seeds = sorted([map(int, inp.readline().split(":")[1].strip().split(" "))])
		inp.readline() # Skip empty line
		for _ in range(7):
			inp.readline() # Skip descriptor line
			mapped = []
			while True:
				line = inp.readline()
				if line.strip() == "":
					break
				destStart, srcStart, rng = map(int, line.split(" "))
				i = 0
				while i < len(seeds):
					# if seeds[i] >= srcStart and seeds[i] < srcStart+rng:
					# 	mapped.append(seeds[i]+(destStart-srcStart))
					# 	seeds.remove(seeds[i])
					# else:
					# 	i += 1
					start = seeds[i][0]
					seedRange = seeds[i][1]
					if start >= srcStart and start+seedRange <= srcStart+rng:
						mapped.append((start+(destStart-srcStart), seedRange))
						seeds.remove(seeds[i])
					elif start >= srcStart and start < srcStart+rng and start+seedRange >= srcStart+rng:
						mapped.append((start+(destStart-srcStart), (srcStart+rng) - start))
						# seeds.append((srcStart+rng, seedRange-((srcStart+rng) - start)))
						seeds.append((srcStart+rng, start+seedRange-(srcStart+rng)))
						seeds.remove(seeds[i])
					elif start < srcStart and start+seedRange <= srcStart+rng and start+seedRange > srcStart:
						mapped.append((destStart, start+seedRange - srcStart))
						seeds.append((start, srcStart-start))
						seeds.remove(seeds[i])
					else:
						i += 1
			for i in seeds:
				mapped.append(i)
			seeds = mapped
		out = -1
		for i in seeds:
			if out == -1 or i[0] < out:
				out = i[0]
		print(out)

if __name__=='__main__':
	run()
