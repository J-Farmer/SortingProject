def pigeonholeSort(arr):
      ma = max(arr)
      mi = min(arr)
      size = max(arr) - mi+1
      holes = [0]*size
     
      for x in arr:
            holes[x-mi]+= 1
      i = 0
      for count in range(size):
            while holes[count]>0:
                  holes[count]-= 1
                  arr[i] = count+mi
                  i += 1

     
    
