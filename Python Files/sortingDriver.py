from timeit import default_timer as timer
from sortingAlgo import bubbleSort, selectionSort, cocktailSort, oddEvenSort


def formatTime(algorithm, time):
	if(time > 60):
		time = time / 60
		print("%s took: %f minutes!" %(algorithm,time))
	else:
		print("%s took: %f seconds!" %(algorithm, time))



arr = []
file = open("../random_numbers.txt")
for lines in file:
    arr.append(int(lines))
file.close()

start = timer()
bubbleSort(arr)
end = timer()
time = round(end-start,3)
formatTime("Bubble Sort", time)

ss = arr
start = timer()
selectionSort(ss)
end = timer()
time = round(end-start,3)
formatTime("Selection Sort", time)

cs = arr
start = timer()
cocktailSort(cs)
end = timer()
time = round(end-start,3)
formatTime("Cocktail Sort", time)

oes = arr
start = timer()
oddEvenSort(oes)
end = timer()
time = round(end-start,3)
formatTime("Odd Even Sort", time)
