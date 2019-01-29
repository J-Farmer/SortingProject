from timeit import default_timer as timer
from sortingAlgo import bubbleSort, selectionSort, cocktailSort, oddEvenSort
from random import randint

def formatTime(algorithm, time):
	if(time > 60):
		time = time / 60
		print("%s took: %f minutes!" %(algorithm,time))
	else:
		print("%s took: %f seconds!" %(algorithm, time))


#Write your file I/O Code here!
arr = []
#for i in range(0,10000):
#    arr.append(randint(-10000,10000))

file = open("../random_numbers.txt")
for lines in file:
    arr.append(int(lines))
file.close()

print("Sorting!")
start = timer()
bubbleSort(arr)#put your function here!
end = timer()

time = round(end-start,3)
formatTime("Bubble Sort", time)


print("Sorting!(Selection Sort)")
ss = arr
start = timer()
selectionSort(ss)#put your function here!
end = timer()
time = round(end-start,3)
formatTime("Selection Sort", time)

print("Sorting!(Cocktail Sort)")
cs = arr
start = timer()
cocktailSort(cs)#put your function here!
end = timer()
time = round(end-start,3)
formatTime("Cocktail Sort", time)

print("Sorting!(Odd Even Sort)")
oes = arr
start = timer()
oddEvenSort(oes)#put your function here!
end = timer()
time = round(end-start,3)
formatTime("Odd Even Sort", time)
