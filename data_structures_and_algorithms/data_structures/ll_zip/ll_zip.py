def zip(First_Linked_List,Second_Linked_List):
    '''
    This Function Take Two LinkedList and Zip the two linked lists together into one
    input-> 
        l1=    <1> <2>  
        l2=    <3> <4>    
    
    output-> 
       <1><3><2><4>
    '''
    if First_Linked_List.linkedList_Lenght()==0 and Second_Linked_List.linkedList_Lenght()==0:
        return 'Lists are empty -> None'

    if First_Linked_List.linkedList_Lenght()==0:
        return Second_Linked_List.__str__()
    
    if Second_Linked_List.linkedList_Lenght()==0:
        return First_Linked_List.__str__()  

    first_pointer=First_Linked_List.head
    first_step=first_pointer.next

    sconde_pointer=Second_Linked_List.head
    second_step=sconde_pointer.next
 

    while first_pointer:
        if sconde_pointer:
            first_pointer.next=sconde_pointer
            first_pointer=first_step
            if first_step:
                first_step=first_step.next
            if first_pointer:
                sconde_pointer.next=first_pointer
                sconde_pointer=second_step
                if second_step:
                    second_step=second_step.next
        else:
            break            

    return First_Linked_List.__str__()
