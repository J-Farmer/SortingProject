from timeit import default_timer as timer
from bubbleSort import bubbleSort #Add your sorting algo under this...
from random import randint

def formatTime(algorithm, time):
	if(time > 60):
		time = time / 60
		print("%s took: %f minutes!" %(algorithm,time))
	else:
		print("%s took: %f seconds!" %(algorithm, time))


#Write your file I/O Code here!
arr = []
for i in range(0,10000):
    arr.append(randint(-10000,10000))


print("Sorting!")
start = timer()
bubbleSort(arr)#put your function here!
end = timer()

time = round(end-start,3)
formatTime("Bubble Sort", time)

#print "Sorting (Bubble Sort) took: ", round(end - start, 3),"seconds!"

#print out a few values here to check!
