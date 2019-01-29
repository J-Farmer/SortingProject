def bubbleSort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
               arr[j],arr[j+1] = arr[j+1],arr[j]

def selectionSort(arr):
    n = len(arr)
    min_idx = 0

    for i in range(0,len(arr)-1):
        min_idx=i

        for j in range(i+1, n):
            if(arr[j] < arr[min_idx]):
                min_idx = j
            arr[min_idx],arr[j] = arr[j],arr[min_idx]

def cocktailSort(arr):
    n = len(arr)
    start = 0
    end = n-1
    swapped = True
    while(swapped == True):
        swapped = False
        for i in range(start,end):
            if(arr[i] > arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
        if(swapped == False):
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if(arr[i] > arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True

        start = start + 1
        
def oddEvenSort(arr):
    n = len(arr)
    for i in range(0,n-1,2):
        if(arr[i] > arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
            
    for i in range(1,n-1,2):
        if(arr[i] > arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]


