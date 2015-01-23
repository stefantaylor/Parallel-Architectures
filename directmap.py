#CAR Assignment 2
#Stefan Taylor
#s1006260
import sys
import math

args = len(sys.argv)
filename = raw_input("Please enter the name of the trace file: ")#sys.argv[1]

#MAIN	---------------------------------------

	#initialise cache


cachesize = 32 * 1024#sys.argv[2] #cachesize in kB
blocksize = 64#int(sys.argv[3], 10)	#blocksize in B
#cachesize = int(cachesize, 10) * 1024
numberofblocks = cachesize / blocksize
cacheblocks=[]
for i in range(numberofblocks):
	cacheblocks = cacheblocks + [0]
blockoffsetbits = math.log(blocksize, 2)
indexbits = math.log(cachesize/blocksize, 2)
tagbits = 48 - (indexbits + blockoffsetbits)





	#read trace file
line = "starto!"
f = open(filename, 'r')
readmisses = 0.0
writemisses = 0.0
totalmisses = 0.0
total = 0.0
readtotal = 0.0
writetotal = 0.0


while line != "":
	line = f.readline()
	if line != "":
		total+=1
		line = line.split()
		instruction = line[1]
		hexaddress = line[2]
		binaddress = bin(int(hexaddress, 16))[2:].zfill(48)
		index = int(binaddress[(48 - int((indexbits+blockoffsetbits))): int((48 - blockoffsetbits))],2)
		tag = binaddress[0: (48 - int((indexbits+blockoffsetbits)))]
		if instruction == "R":
			readtotal+=1
		elif instruction == "W":
			writetotal+=1
		if cacheblocks[index] != tag:
			if instruction == "R":
				readmisses+=1
			elif instruction == "W":
				writemisses+=1
			totalmisses+=1
			cacheblocks[index]=tag

print("Total Miss Rate = " + str(totalmisses/total*100) + " %")
print("Write Miss Rate = " + str(writemisses/writetotal*100) + " %")
print("Read Miss Rate = " + str(readmisses/readtotal*100) + " %")

print("done")
