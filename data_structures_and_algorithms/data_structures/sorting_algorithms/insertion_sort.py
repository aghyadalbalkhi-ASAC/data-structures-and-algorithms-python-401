def insertionSort(arr): 
    # loop through array elements [from 1 to last element]

    if len(arr) == 0:
        raise AttributeError ('Array is empty')
    for i in range(len(arr)):

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
    return arr


if __name__ == '__main__':
    arr = [10,77,23,55,2]
    print(insertionSort(arr))