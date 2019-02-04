def shellSort(arr):
   
    x = len(arr)
    gap = x//2

    while gap > 0:
        for i in range(gap, x):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j-=gap
            arr[j] = temp
        gap //= 2

            
    
 
