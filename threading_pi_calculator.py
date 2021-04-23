from threading import Thread
import sys

def calculatePI(ini, nThreads, nTerms, resultList):
	pi = 0	
	for i in range(ini, nTerms, nThreads):
		term = 1.0/(2*i-1)
		pi += term if i % 2 == 1 else -term

	resultList.append(pi * 4)

if (len(sys.argv) != 3):
	print('%s <num_terms> <num_threads>' % sys.argv[0])
	sys.exit(0)

nTerms = int(sys.argv[1])
nThreads = int(sys.argv[2])

threadsList = []
resultList = []

for i in range(nThreads):
	threadsList.append(Thread(
		target=calculatePI,
		args=[i+1, nThreads, nTerms, resultList]
	))
	threadsList[-1].start()

for thread in threadsList:
	thread.join()

print('PI: %.15f' % sum(resultList))