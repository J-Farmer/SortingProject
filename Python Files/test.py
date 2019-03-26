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

#file = open("../runtimes.csv","a")

largeBSTime = []
largeOESTime = []
for i in range(100, 15000, 100):
        num = []
        bstime = 0
        oestime = 0
        for j in range(0,i):
                num.append(randint(-10000,10000))
                
        for k in range(0,100):
                bs = num[:]
                start = timer()
                bubbleSort(num)
                end = timer()
                bstime = bstime + round(end - start,3)

                oes = num[:]
                start = timer()
                oddEvenSort(oes)
                end = timer()
                oestime = oestime + round(end - start,3)
                
        largeBSTime.append(bstime / 100)
        largeOESTime.append(oestime / 100)
        print("Bubble Sort",str(i)+":","took",round((bstime / 100),3),"seconds!")
        print("Odd Even Sort",str(i)+":","took",round((oestime / 100),3),"seconds!")
        #file.write(str(time)+"\n")

#file.close()
plt.plot(largeBSTime)
plt.plot(largeOESTime)
plt.show()
