from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Queue



def DuckDuckGoose(list_of_string,k):
    """
    DuckDuckGoose() function that accepts a list of strings and an int k.
    Start at the beginning of the list and count up to k and remove the person at that index from the list.
    Keep counting from that index and count up to k over and over until only one person is left in the list.
    Return a string with the name of the last person left in the list.
    """

    # size to track the number of elements for En_queue Elements
    size = len(list_of_string)

    # This counter for to determine the next target element in the circle Game  -> k = 3 , move until reach count 3 and reset again
    count = 1

    # Queue 
    duck = Queue()

    # This list contain the Elements that are out of the game  // For checking through looping and skip these elements
    removeal =[]

    # en_queue the elements of list 
    for i in range(size):
        duck.enqueue(list_of_string[i])

    # mover to loop over the queue and over again Even if reachs the end
    mover = duck.front

    # Keeping loop untill size zero // or u can make it a {1} it will give the same resutl but keept it zero to get the left element
    while size!=0:

        # skip the element if it kick out of the game and jump to the next one
        if mover.value in removeal:
            mover=mover.next

        # if we reach to the target Element - append to the removale list (its like kick it out of the game) and reset the counter
        # jumpt to the next Element
        elif count == k :
            removeal.append(mover.value)
            size-=1
            count=1
            mover=mover.next

        # if the element isnt the target one or one of the removeal elements
        else:
            count+=1
            mover=mover.next

        # if the mover reach the end of queue back to the beginning again
        if mover ==None:
            mover =duck.front  
    # print(size)
    # print(removeal)
    return(f'only {removeal[-1]} is left')


if __name__ == "__main__":
    list_of_string = ['A','B','C','D','E']
    k = 4 
    print(DuckDuckGoose(list_of_string,k))