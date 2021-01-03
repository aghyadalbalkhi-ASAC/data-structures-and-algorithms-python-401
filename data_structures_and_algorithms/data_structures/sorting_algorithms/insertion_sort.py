def insertionSort(arr): 
    # loop through array elements [from 1 to last element]
    
        #point to the last sorted element
        j = i-1
        
        # the first unsorted element
        temp = arr[i] 
        
        # shift element while the unsorted element less than current sorted element
        while j >= 0 and temp < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
                
        # replace the value of current element with unsorted one 
        arr[j + 1] = temp 