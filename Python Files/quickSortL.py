def partition(arr,lo,hi):
    pvt=arr[hi]
    i=lo-1
    f=hi
    for f in range(lo,hi):
        if arr[f]<=pvt:
            i=i+1
            arr[i],arr[f]=arr[f],arr[i]
    arr[i+1],arr[hi]=arr[hi],arr[i+1]
    return(i+1)

def quickSort(arr,lo,hi):
    if lo<hi:
        p=partition(arr,lo,hi)
        quickSort(arr,lo,p-1)
        quickSort(arr,p+1,hi)
