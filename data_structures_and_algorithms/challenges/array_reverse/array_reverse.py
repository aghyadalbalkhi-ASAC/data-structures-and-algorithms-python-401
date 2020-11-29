def reverse_array(arr):
    """Reverses a list

    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    returnedArr =[]
    lengthOfArray=len(arr)
    while lengthOfArray :
        returnedArr.append(arr[lengthOfArray-1])
        lengthOfArray-=1
    return returnedArr


testArray=[1,2,3,4,5,6]
print(reverse_array(testArray))    