datasummary = {}
datakeys []
def readdata () :
	global datakeys, datasummary
	f1 = open('input.txt', 'r')
	line f1.readline()
	while (line):
		data line.strip() .split(",")
		for dataitern in data:
			if dataitern in datasummary:
				datasummary [dataitern] += 1
			else:
				datasummary[dataitern] = 1
				datakeys =datakeys + [dataitern]
		line f1.readline()
	fl.close ()
def processdata():
	global datakeys
	for i in range (len (datakeys) i) :
		for j in range (i+1, len(datakeys»:
			if (datakeys [i] > datakeys[j]):
				datakeys[i], datakeys[j] datakeys[j], datakeys[i]
def printdata():
	global datakeys, datasummary
	f2 open ( 'output. txt' , 'w')
	for key in datakeys:
		f2.write('{}-{}\n' .format(keY,datasummary[key]»
	f2 .close ()
readdata( )
processdata-( )
printdata ()