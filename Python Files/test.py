from timeit import default_timer as timer
from random import randint
from sortingAlgo import bubbleSort, selectionSort, cocktailSort, oddEvenSort
from pigeonhole_Sort import pigeonholeSort
from shellSort import shellSort
from quickSort import quickSort
import quickSortH, quickSortL
import matplotlib.pyplot as plt

def formatTime(algorithm, time):
	if(time > 60):
		time = time / 60
		print("%s took: %s minutes!" %(algorithm,time))
	else:
		print("%s took: %s seconds!" %(algorithm, time))


arr = []
file = open("../random_numbers.txt")
for lines in file:
    arr.append(int(lines))
file.close()
del file

file = open("../runtimes.csv","a")

largeTime = []
for i in range(100, 10000, 100):
        num = []
        time = 0
        for j in range(0,i):
                num.append(randint(-10000,10000))
                
        for k in range(0,100):        
                start = timer()
                bubbleSort(num)
                end = timer()
                
                time = time + round(end - start,3)
        largeTime.append(time / 100)
        print("Bubble Sort",str(i)+":","took",round((time / 100),3),"seconds!")
        file.write(str(time)+"\n")

file.close()
plt.plot(largeTime)
plt.show()
