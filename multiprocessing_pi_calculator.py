from multiprocessing import Process, Queue
import sys

def calculatePI(ini, nProcess, nTerms, queueResult):
	pi = 0	
	for i in range(ini, nTerms, nProcess):
		term = 1.0/(2*i-1)
		pi += term if i % 2 == 1 else -term

	queueResult.put(pi * 4)
	

if (len(sys.argv) != 3):
	print('%s <num_terms> <num_process>' % sys.argv[0])
	sys.exit(0)

nTerms = int(sys.argv[1])
nProcess = int(sys.argv[2])

processList = []
queueResult = Queue()

for i in range(nProcess):
	processList.append(Process(
		target=calculatePI,
		args=[i+1, nProcess, nTerms, queueResult]
	))
	processList[-1].start()


for process in processList:
	process.join()

pi = 0
while not queueResult.empty():
	pi += queueResult.get()

print('PI: %.15f' % pi)