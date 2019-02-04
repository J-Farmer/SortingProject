def partition(arr, lo, hi):
    pivot = arr[hi]

    i = lo - 1

    for j in range(lo, hi):
        if(arr[j] <= pivot):
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[hi] = arr[hi],arr[i+1]
    return i + 1

def quickSort(arr, lo, hi):
    if(lo<hi):
        pi = partition(arr,lo,hi)
        quickSort(arr,lo,pi-1)
        quickSort(arr,pi+1,hi)
