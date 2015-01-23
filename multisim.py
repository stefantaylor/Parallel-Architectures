#PA Assignment 2
#Stefan Taylor
#s1006260
import sys
import math

filename = "trace2.txt"#raw_input("\nPlease enter the name of the trace file:\n\n>>> ")
cachesize = 32#int(raw_input("\nPlease enter the size of the cache (in KB):\n\n>>> "))
linesize = 64#int(raw_input("\nPlease enter the size of the cache lines (in Bytes):\n\n>>> "))
mesi = int(raw_input("\nWould you like to use MSI or MESI protocol?\n\nType 0 for MSI or 1 for MESI.\n\n>>> "))
cachelines = cachesize * 1024 / linesize
offsetbits = int(math.log(linesize, 2))
indexbits = int(math.log(cachelines, 2))

readmisses = 0.0
writemisses = 0.0
totalmisses = 0.0
total = 0.0
readtotal = 0.0
silentwrites = 0
writetotal = 0.0
invalidates = 0
totalinvalidates = 0


cache0 = [(0, "I")] * cachelines #initialise list to model the cache for processor 0
cache1 = [(0, "I")] * cachelines #initialise list to model the cache for processor 1
cache2 = [(0, "I")] * cachelines #initialise list to model the cache for processor 2
cache3 = [(0, "I")] * cachelines #initialise list to model the cache for processor 3

with open(filename, 'r') as f:
	print "\nFile Found"
	print "\nSimulating..."
	if mesi ==0:

###################################################################

############################### MSI ###############################

###################################################################

		for line in f:
			total += 1
			line = (line.strip()).split()
			if len(line) == 2:	
				i = line[0]
				m = line[1]
			else:
				p = int(line[0][1])
				i = line[1]
				m = line[2]
			hexaddr = int(m, 16)
			binaddr = bin(hexaddr)[2:].zfill(48)
			offset = binaddr[-offsetbits:]
			index = int(binaddr[-(offsetbits+indexbits):-offsetbits],2)
			tag = binaddr[:-(offsetbits+indexbits)]

			### Processor 0
			if p == 0:

				if cache0[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache0[index] = (tag, "I")

				if cache0[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Cache Value
						cache0[index] = (tag, "S")
						#Set other Caches to be shared where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "S")
						if cache2[index][0] == tag:
							cache2[index] = (tag, "S")
						if cache3[index][0] == tag:
							cache3[index] = (tag, "S")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache0[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "I")
							invalidates += 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "I")
							invalidates += 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "I")
							invalidates += 1

				elif cache0[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache0[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache0[index] = (tag, "M")

				elif cache0[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache0[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache0[index] = (tag, "M")

			### Processor 1
			if p == 1:

				if cache1[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache1[index] = (tag, "I")

				if cache1[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Cache Value
						cache1[index] = (tag, "S")
						#Set other Caches to be shared where necessary
						if cache0[index][0] == tag:
							cache0[index] = (tag, "S")
						if cache2[index][0] == tag:
							cache2[index] = (tag, "S")
						if cache3[index][0] == tag:
							cache3[index] = (tag, "S")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache1[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache0[index][0] == tag:
							cache0[index] = (tag, "I")
							invalidates += 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "I")
							invalidates += 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "I")
							invalidates += 1

				elif cache1[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache1[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache1[index] = (tag, "M")

				elif cache1[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache1[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache1[index] = (tag, "M")

			### Processor 2
			if p == 2:

				if cache2[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache2[index] = (tag, "I")

				if cache2[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Cache Value
						cache2[index] = (tag, "S")
						#Set other Caches to be shared where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "S")
						if cache0[index][0] == tag:
							cache0[index] = (tag, "S")
						if cache3[index][0] == tag:
							cache3[index] = (tag, "S")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache2[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "I")
							invalidates += 1
						if cache0[index][0] == tag:
							cache0[index] = (tag, "I")
							invalidates += 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "I")
							invalidates += 1

				elif cache2[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache2[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache2[index] = (tag, "M")

				elif cache2[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache2[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache2[index] = (tag, "M")

			### Processor 3
			if p == 3:

				if cache3[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache3[index] = (tag, "I")

				if cache3[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Cache Value
						cache3[index] = (tag, "S")
						#Set other Caches to be shared where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "S")
						if cache2[index][0] == tag:
							cache2[index] = (tag, "S")
						if cache0[index][0] == tag:
							cache0[index] = (tag, "S")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache3[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "I")
							invalidates += 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "I")
							invalidates += 1
						if cache0[index][0] == tag:
							cache0[index] = (tag, "I")
							invalidates += 1

				elif cache3[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache3[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache3[index] = (tag, "M")

				elif cache3[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache3[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache3[index] = (tag, "M")


##################################################################

############################## MESI ##############################

##################################################################



	elif mesi == 1:
		for line in f:
			shared = 0
			total += 1
			line = (line.strip()).split()
			if len(line) == 2:	
				i = line[0]
				m = line[1]
			else:
				p = int(line[0][1])
				i = line[1]
				m = line[2]
			hexaddr = int(m, 16)
			binaddr = bin(hexaddr)[2:].zfill(48)
			offset = binaddr[-offsetbits:]
			index = int(binaddr[-(offsetbits+indexbits):-offsetbits],2)
			tag = binaddr[:-(offsetbits+indexbits)]

			### Processor 0
			if p == 0:

				if cache0[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache0[index] = (tag, "I")

				if cache0[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Check whether other caches share the value, and set Shared where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "S")
							shared = 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "S")
							shared = 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "S")
							shared = 1
						#Cache Value. If it was shared set S, else set E
						if shared == 1:
							cache0[index] = (tag, "S")
						else:
							cache0[index] = (tag, "E")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache0[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "I")
							invalidates += 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "I")
							invalidates += 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "I")
							invalidates += 1

				elif cache0[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache0[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache0[index] = (tag, "M")

				elif cache0[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache0[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache0[index] = (tag, "M")

				elif cache0[index][1] == "E":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache0[index] = (tag, "E")
					elif i == "W":
						writetotal += 1
						silentwrites += 1
						cache0[index] = (tag, "M")

			### Processor 1
			if p == 1:

				if cache1[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache1[index] = (tag, "I")

				if cache1[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Check whether other caches share the value, and set Shared where necessary
						if cache0[index][0] == tag:
							cache0[index] = (tag, "S")
							shared = 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "S")
							shared = 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "S")
							shared = 1
						#Cache Value. If it was shared set S, else set E
						if shared == 1:
							cache1[index] = (tag, "S")
						else:
							cache1[index] = (tag, "E")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache1[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache0[index][0] == tag:
							cache0[index] = (tag, "I")
							invalidates += 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "I")
							invalidates += 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "I")
							invalidates += 1

				elif cache1[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache1[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache1[index] = (tag, "M")

				elif cache1[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache1[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache1[index] = (tag, "M")

				elif cache1[index][1] == "E":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache1[index] = (tag, "E")
					elif i == "W":
						writetotal += 1
						silentwrites += 1
						cache1[index] = (tag, "M")

			### Processor 2
			if p == 2:

				if cache2[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache2[index] = (tag, "I")

				if cache2[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Check whether other caches share the value, and set Shared where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "S")
							shared = 1
						if cache0[index][0] == tag:
							cache0[index] = (tag, "S")
							shared = 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "S")
							shared = 1
						#Cache Value. If it was shared set S, else set E
						if shared == 1:
							cache2[index] = (tag, "S")
						else:
							cache2[index] = (tag, "E")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache2[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "I")
							invalidates += 1
						if cache0[index][0] == tag:
							cache0[index] = (tag, "I")
							invalidates += 1
						if cache3[index][0] == tag:
							cache3[index] = (tag, "I")
							invalidates += 1

				elif cache2[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache2[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache2[index] = (tag, "M")

				elif cache2[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache2[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache2[index] = (tag, "M")

				elif cache2[index][1] == "E":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache2[index] = (tag, "E")
					elif i == "W":
						writetotal += 1
						silentwrites += 1
						cache2[index] = (tag, "M")

			### Processor 3
			if p == 3:

				if cache3[index][0] != tag:
					#if the cache entry is not the right one (tags don't match), invalidate it
					cache3[index] = (tag, "I")

				if cache3[index][1] == "I":
					#Any transactions from the invalid state can be assumed to be misses
					totalmisses += 1
					if i == "R":
						readmisses+=1
						readtotal+=1
						#Check whether other caches share the value, and set Shared where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "S")
							shared = 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "S")
							shared = 1
						if cache0[index][0] == tag:
							cache0[index] = (tag, "S")
							shared = 1
						#Cache Value. If it was shared set S, else set E
						if shared == 1:
							cache3[index] = (tag, "S")
						else:
							cache3[index] = (tag, "E")

					elif i == "W":
						writetotal +=1
						writemisses +=1
						#Cache Value
						cache3[index] = (tag, "M")
						#Set other Caches to be invalid where necessary
						if cache1[index][0] == tag:
							cache1[index] = (tag, "I")
							invalidates += 1
						if cache2[index][0] == tag:
							cache2[index] = (tag, "I")
							invalidates += 1
						if cache0[index][0] == tag:
							cache0[index] = (tag, "I")
							invalidates += 1

				elif cache3[index][1] == "S":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache3[index] = (tag, "S")
					elif i == "W":
						writetotal += 1
						cache3[index] = (tag, "M")

				elif cache3[index][1] == "M":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache3[index] = (tag, "M")
					elif i == "W":
						writetotal += 1
						cache3[index] = (tag, "M")

				elif cache3[index][1] == "E":
					#any transactions from this state will be a hit
					if i == "R":
						readtotal += 1
						cache3[index] = (tag, "E")
					elif i == "W":
						writetotal += 1
						silentwrites += 1
						cache3[index] = (tag, "M")

	else:
		print("Error. Please enter 0 or 1 for whether to use MSI or MESI protocol")



			



dashstr = "-" * 50
print("\n" + dashstr)		
print("Total Miss Rate = " + str(totalmisses/total*100) + " %")
print("\nWrite Miss Rate = " + str(writemisses/writetotal*100) + " %")
print("\nRead Miss Rate = " + str(readmisses/readtotal*100) + " %")
print("\nTotal Invalidations = " + str(invalidates))
if silentwrites > 0:
	print("\nNumber of writes which are silent = " + str(silentwrites))
print(dashstr)		
print("\nDone\n \n")



		
# SO apparantly I don't do DRY. Oh well, maybe next time.	
