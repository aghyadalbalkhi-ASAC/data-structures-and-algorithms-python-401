


def array_binarySearch(array,target): 
    startPoint=0
    endPoint=len(array)-1
    mid=0
    # Check base case 
    while endPoint >= startPoint:
  
        mid = (endPoint + startPoint) // 2
  
        # check the target if is in the middel or Not 
        if array[mid] == target: 
            return mid 
  
        # If Not check the target value location


        # if mid greater than the target  
        # set the mid point as the end point -1 becuse we check the mid at the beginning  
        if array[mid] > target: 
            endPoint=mid-1
  
        # if mid smaller than the target  
        # set the mid point as the start point +1 becuse we check the mid at the beginning  
        else: 
            startPoint=mid+1        
   
    # value Not Found
    return -1


if __name__ == "__main__":
    array = [ 25, 35, 65, 80, 85,86,96,97,98,102,111 ] 
    target = 103

    index = array_binarySearch(array,target) 
    
    if index != -1: 
        print("value found at index", index) 
    else: 
        print("value Not Found") 