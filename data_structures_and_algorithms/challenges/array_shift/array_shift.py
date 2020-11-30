import math

def insertShiftArray(array,value):
    lenOfArray= len(array)
    indexOfInsert = math.ceil(lenOfArray/2)
    print(indexOfInsert)
    newArr =[]
    index=0
    for i in range(lenOfArray+1):
        if i == indexOfInsert:
            newArr.append(value)
        else:
            newArr.append(array[index])
            index+=1
    return newArr

arr=[4,8,15,23,42]
print(insertShiftArray(arr,16))