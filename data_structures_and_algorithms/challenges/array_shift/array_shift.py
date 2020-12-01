import math

def insertShiftArray(array,value):

    #validation Test
    if len(array)== 0 or len(array)==1:
        array.append(value)
        return array
    else :
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


def insertShiftArray2(array,value):
    #validation Test
    if len(array)== 0 or len(array)==1:
        array.append(value)
        return array
    else:
        # lastEle = len(array)-1    Orginal Length before increse sizq
        middel = math.ceil(len(array)/2) #define the Middel
        lastIndex = len(array)      #last Index in the array after append ele(0)
        array.append(0)         #increase the size
        n =len(array)           # length of array 
        while n>middel :        # it while stop at middel index
            array[lastIndex]=array[lastIndex-1]             #swap values betweeb the ele and its pre
            lastIndex-=1
            n-=1
        array[middel]=value
        return array
    
    
insertShiftArray2([4,8,15,23,42],16)