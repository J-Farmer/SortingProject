from timeit import default_timer as timer
from sortingAlgo import bubbleSort, selectionSort, cocktailSort, oddEvenSort
from pigeonhole_Sort import pigeonholeSort
from shellSort import shellSort
from quickSort import quickSort
import quickSortH, quickSortL
from combSort import combSort
from insertionSort import insertionSort

def formatTime(algorithm, time):
	if(time > 60):
		time = time / 60
		print("%s took: %s minutes!" %(algorithm,time))
	else:
		print("%s took: %s seconds!" %(algorithm, time))

for i in range(100,8000,100):
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
	cbsTime = []
	isTime = []

	for k in range(0,100):
			
			bigStart = timer()
			
			bs = arr[:i]
			print(bs)
			start = timer()
			bubbleSort(bs)
			end = timer()
			time = round(end-start,3)
			bsTime.append(time)
			formatTime("Bubble Sort", time)
			del bs

			ss = arr[:i]
			start = timer()
			selectionSort(ss)
			end = timer()
			time = round(end-start,3)
			ssTime.append(time)
			formatTime("Selection Sort", time)
			del ss

			cs = arr[:i]
			start = timer()
			cocktailSort(cs)
			end = timer()
			time = round(end-start,3)
			csTime.append(time)
			formatTime("Cocktail Sort", time)
			del cs

			oes = arr[:i]
			start = timer()
			oddEvenSort(oes)
			end = timer()
			time = round(end-start,3)
			oesTime.append(time)
			formatTime("Odd Even Sort", time)
			del oes
			
			phs = arr[:i]
			start = timer()
			pigeonholeSort(phs)
			end = timer()
			time = round(end-start,3)
			phsTime.append(time)
			formatTime("Pigeonhole Sort", time)
			del phs
			
			shs = arr[:i]
			start = timer()
			shellSort(shs)
			end = timer()
			time = round(end-start,3)
			shsTime.append(time)
			formatTime("Shell Sort", time)
			del shs
			
			qsH = arr[:i]
			start = timer()
			quickSortH.quickSort(qsH, 0, len(qsH)-1)
			end = timer()
			time = round(end-start,3)
			qsHTime.append(time)
			formatTime("Quick Sort (Hoare)", time)
			del qsH
			
			qsL = arr[:i]
			start = timer()
			quickSortL.quickSort(qsL, 0, len(qsL)-1)
			end = timer()
			time = round(end-start,3)
			qsLTime.append(time)
			formatTime("Quick Sort (Lomuto)", time)
			del qsL
			
			cbs = arr[:i]
			start = timer()
			combSort(cbs)
			end = timer()
			time = round(end-start,3)
			cbsTime.append(time)
			formatTime("Comb Sort", time)
			del cbs

			iss = arr[:i]
			start = timer()
			insertionSort(iss)
			end = timer()
			time = round(end-start,3)
			isTime.append(time)
			formatTime("Insertion Sort", time)
			del iss
			
			bigEnd = timer()
			time = round(bigEnd-bigStart,3)
			formatTime(str(i+1), time)

	formatTime("Bubble Sort", round(sum(bsTime)/len(bsTime),3))
	formatTime("Selection Sort", round(sum(ssTime)/len(ssTime),3))
	formatTime("Cocktail Sort", round(sum(csTime)/len(csTime),3))
	formatTime("Odd Even Sort", round(sum(oesTime)/len(oesTime),3))
	formatTime("Pigeonhole Sort", round(sum(phsTime)/len(phsTime),3))
	formatTime("Shell Sort", round(sum(shsTime)/len(shsTime),3))
	formatTime("Quick Sort (H) Sort", round(sum(qsHTime)/len(qsHTime),3))
	formatTime("Quick Sort (L) Sort", round(sum(qsLTime)/len(qsLTime),3))
	formatTime("Comb Sort", round(sum(cbsTime)/len(cbsTime),3))
	formatTime("Insertion Sort", round(sum(isTime)/len(isTime),3))

del bigEnd
del arr
del time
