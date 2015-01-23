#PA Assignment 2
#Stefan Taylor
#s1006260
import sys
import math


filename = "trace1.txt"#raw_input("\nPlease enter the name of the trace file:\n\n>>> ")
cachesize = 32#int(raw_input("Please enter the size of the cache (in KB): "))
linesize = 64#int(raw_input("Please enter the size of the cache lines (in Bytes): "))
cachelines = cachesize * 1024 / linesize
offsetbits = int(math.log(linesize, 2))
indexbits = int(math.log(cachelines, 2))

P = 0

readmisses = 0.0
writemisses = 0.0
totalmisses = 0.0
total = 0.0
readtotal = 0.0
writetotal = 0.0

cache = [(0, "I")] * cachelines #initialise list to model the cache
cache0 = [(0, "I")] * cachelines #initialise list to model the cache
cache1 = [(0, "I")] * cachelines #initialise list to model the cache
cache2 = [(0, "I")] * cachelines #initialise list to model the cache
cache3 = [(0, "I")] * cachelines #initialise list to model the cache

with open(filename, 'r') as f:
	print "\nFile Found"
	print "\nSimulating..."
	for line in f:
		total += 1
		line = (line.strip()).split()
		if len(line) == 2:	
			i = line[0]
			m = line[1]
		else:
			p = line[0]
			i = line[1]
			m = line[2]
		hexaddr = int(m, 16)
		binaddr = bin(hexaddr)[2:].zfill(32)
		offset = binaddr[-offsetbits:]
		index = int(binaddr[-(offsetbits+indexbits):-offsetbits],2)
		tag = binaddr[:-(offsetbits+indexbits)]

		if i == "R":
			readtotal+=1
		elif i == "W":
			writetotal+=1
		if cache[index][0] != tag:
			if i == "R":
				readmisses+=1
			elif i == "W":
				writemisses+=1
			totalmisses+=1
			cache[index]=(tag, "M")

dashstr = "-" * 50
print("\n" + dashstr)		
print("Total Miss Rate = " + str(totalmisses/total*100) + " %")
print("\nWrite Miss Rate = " + str(writemisses/writetotal*100) + " %")
print("\nRead Miss Rate = " + str(readmisses/readtotal*100) + " %")
print(dashstr)		
print("\nDone\n \n")



		
		
