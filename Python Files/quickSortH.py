def partition(arr,lo,hi):
    pvt=arr[lo]
    i=lo-1
    f=hi+1
    while True:
        i=i+1
        while arr[i]<pvt:
            i=i+1
        f=f-1
        while arr[f]>pvt:
            f=f-1
        if i>=f:
            return(f)
        arr[i],arr[f]=arr[f],arr[i]

def quickSort(arr,lo,hi):
    if lo<hi:
        p=partition(arr,lo,hi)
        quickSort(arr,lo,p)
        quickSort(arr,p+1,hi)
