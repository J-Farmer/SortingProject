def combSort(arr): 
    c = len(arr)

    gap = c
    shrink = 1.3 
    swapped = True
    
    while(gap > 1 and swapped == True):

        swapped = False
        gap = int(gap / shrink)
        
        if(gap < 1):
            gap = 1

        for i in range(0, c-gap):
            if (arr[i] > arr[i + gap]):
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
        





  
