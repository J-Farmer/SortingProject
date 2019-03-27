from timeit import default_timer as timer
from random import randint
from sortingAlgo import bubbleSort, selectionSort, cocktailSort, oddEvenSort
from pigeonhole_Sort import pigeonholeSort
from shellSort import shellSort
from quickSort import quickSort
import quickSortH, quickSortL
from combSort import combSort
from insertionSort import insertionSort
import matplotlib.pyplot as plt
import numpy as np

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
largeCSTime = []
largeSSTime = []
largePHSTime = []
largeQSTime = []
largeCBSTime = []
largeSHSTime = []
largeISSTime = []

for i in range(100, 2100, 100):
        print(i)
        num = []
        bstime = 0
        oestime = 0
        cstime = 0
        sstime = 0
        phstime = 0
        shstime = 0
        qstime = 0
        cbstime = 0
        isstime = 0
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

                cs = num[:]
                start = timer()
                cocktailSort(cs)
                end = timer()
                cstime = cstime + round(end - start,3)

                ss = num[:]
                start = timer()
                selectionSort(ss)
                end = timer()
                sstime = sstime + round(end - start,3)

                phs = num[:]
                start = timer()
                pigeonholeSort(phs)
                end = timer()
                phstime = phstime + round(end - start,3)

                shs = num[:]
                start = timer()
                shellSort(shs)
                end = timer()
                shstime = shstime + round(end - start,3)

                #qs = num[:]
                #start = timer()
                #quickSortH.quickSort(qs, 0, len(qs) - 1)
                #end = timer()
                #qstime = qstime + round(end - start,3)

                cbs = num[:]
                start = timer()
                combSort(cbs)
                end = timer()
                cbstime = cbstime + round(end - start,3)

                iss = num[:]
                start = timer()
                insertionSort(iss)
                end = timer()
                isstime = isstime + round(end - start,3)
                
        largeBSTime.append(bstime / 100)
        largeOESTime.append(oestime / 100)
        largeCSTime.append(cstime / 100)
        largeSSTime.append(sstime / 100)
        largePHSTime.append(phstime / 100)
        largeSHSTime.append(shstime / 100)
        largeQSTime.append(qstime / 100)
        largeCBSTime.append(cbstime / 100)
        largeISSTime.append(isstime / 100)
        #file.write(str(time)+"\n")

#file.close()
plt.plot(largeBSTime, label = "Bubble Sort")
plt.plot(largeOESTime, label = "Odd Even Sort")
plt.plot(largeCSTime, label = "Cocktail Shaker Sort")
plt.plot(largeSSTime, label = "Selection Sort")
plt.plot(largePHSTime, label = "Pigeonhole Sort")
plt.plot(largeSHSTime, label = "Shell Sort")
plt.plot(largeQSTime, label = "Quick Sort")
plt.plot(largeCBSTime, label = "Comb Sort")
plt.plot(largeISSTime, label = "Insertion Sort")
plt.legend()
plt.show()
