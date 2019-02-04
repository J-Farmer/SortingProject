from timeit import default_timer as timer
from sortingAlgo import bubbleSort, selectionSort, cocktailSort, oddEvenSort
from pigeonhole_Sort import pigeonholeSort
from shellSort import shellSort
from quickSort import quickSort
import quickSortH, quickSortL

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

bsTime = []
ssTime = []
csTime = []
oesTime = []
phsTime = []
shsTime = []
qsHTime = []
qsLTime = []

for i in range(0,100):
        print(i)
        bigStart = timer()
        
        bs = arr[:]
        start = timer()
        bubbleSort(bs)
        end = timer()
        time = round(end-start,3)
        bsTime.append(time)
        #formatTime("Bubble Sort", time)
        del bs

        ss = arr[:]
        start = timer()
        selectionSort(ss)
        end = timer()
        time = round(end-start,3)
        ssTime.append(time)
        #formatTime("Selection Sort", time)
        del ss

        cs = arr[:]
        start = timer()
        cocktailSort(cs)
        end = timer()
        time = round(end-start,3)
        csTime.append(time)
        #formatTime("Cocktail Sort", time)
        del cs

        oes = arr[:]
        start = timer()
        oddEvenSort(oes)
        end = timer()
        time = round(end-start,3)
        oesTime.append(time)
        #formatTime("Odd Even Sort", time)

        phs = arr[:]
        start = timer()
        pigeonholeSort(phs)
        end = timer()
        time = round(end-start,3)
        phsTime.append(time)
        #formatTime("Pigeonhole Sort", time)

        shs = arr[:]
        start = timer()
        shellSort(shs)
        end = timer()
        time = round(end-start,3)
        shsTime.append(time)
        #formatTime("Shell Sort", time)

        qsH = arr[:]
        start = timer()
        quickSortH.quickSort(qsH, 0, len(qsH)-1)
        end = timer()
        time = round(end-start,3)
        qsHTime.append(time)
        #formatTime("Quick Sort (Hoare)", time)

        qsL = arr[:]
        start = timer()
        quickSortL.quickSort(qsL, 0, len(qsL)-1)
        end = timer()
        time = round(end-start,3)
        qsLTime.append(time)
        #formatTime("Quick Sort (Lomuto)", time)
        
        bigEnd = timer()
        time = round(bigEnd-bigStart,3)
        print(time)


formatTime("Bubble Sort", sum(bsTime)/len(bsTime))
formatTime("Selection Sort", sum(ssTime)/len(ssTime))
formatTime("Cocktail Sort", sum(csTime)/len(csTime))
formatTime("Odd Even Sort", sum(oesTime)/len(oesTime))
formatTime("Pigeonhole Sort", sum(phsTime)/len(phsTime))
formatTime("Shell Sort", sum(shsTime)/len(shsTime))
formatTime("Quick Sort (H) Sort", sum(qsHTime)/len(qsHTime))
formatTime("Quick Sort (L) Sort", sum(qsLTime)/len(qsLTime))

del phs
del shs
del oes
del arr
del time
