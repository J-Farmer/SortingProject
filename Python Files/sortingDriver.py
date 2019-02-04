from timeit import default_timer as timer
from sortingAlgo import bubbleSort, selectionSort, cocktailSort, oddEvenSort
from pigeonhole_Sort import pigeonholeSort
from shellSort import shellSort

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
del file

print(arr[::100])

bs = arr[:]
start = timer()
bubbleSort(bs)
end = timer()
time = round(end-start,3)
formatTime("Bubble Sort", time)
del bs

ss = arr[:]
start = timer()
selectionSort(ss)
end = timer()
time = round(end-start,3)
formatTime("Selection Sort", time)
del ss

cs = arr[:]
start = timer()
cocktailSort(cs)
end = timer()
time = round(end-start,3)
formatTime("Cocktail Sort", time)
del cs

oes = arr[:]
start = timer()
oddEvenSort(oes)
end = timer()
time = round(end-start,3)
formatTime("Odd Even Sort", time)

phs = arr[:]
start = timer()
pigeonholeSort(phs)
end = timer()
time = round(end-start,3)
formatTime("Pigeonhole Sort", time)

shs = arr[:]
start = timer()
shellSort(shs)
end = timer()
time = round(end-start,3)
formatTime("Shell Sort", time)

del phs
del shs
del oes
del arr
del time
