class Node:
    """ 
    Node class Create Objects that has properties for the value stored in the Node, and a pointer to the next Node.
    """
    #initialize the constructor
    def __init__(self, value):
        self.value = value
        self.next = None

    #This Method called when print or use the object it self (similar to to string method)
    def __repr__(self):
        return f'{{ {self.value} }}'

class LinkedList:

    """
    A Linked List is a sequence of Nodes that are connected/linked to each other.
    The most defining feature of a Linked List is that each Node references the next Node in the link.
    """

    #initialize an empty linke list with head -> Null
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,value):
        """
        The append method Take value as an argument then create a node to append this node at the end of this list
        """
        # Creating Node and setting the value
        new_node = Node(value)

        #edge Case to add the node as  a head if the LinkedList Is Empty
        if not self.head:
            self.head = new_node
        else :
            current_Node = self.head        #set the node_pointer which is looping over the LinkeList

            while current_Node.next != None:    #moving until the last node where last node .next will refer to None
                current_Node = current_Node.next    #Transfer to the next node
            current_Node.next = new_node                 # outter of loop to add the node

    def insertBefore(self,value, newVal):
        """
        Add a new node with the given newValue immediately Befor the first value node
        """             
        new_node = Node(newVal)             #create New Node
        if not self.includes(value):                   # if LinkedList Empty
            return "Value Not Found"
        elif self.head.value == value:      # if the value in the Head insert at the first 
            self.insert(newVal)
        else :                                  
            current_Node = self.head        #set the node_pointer which is looping over the LinkeList
            while current_Node.next != None:    
                if current_Node.next.value == value:    #check the value of next node before moving
                    new_node.next = current_Node.next   # link the new_node first
                    current_Node.next = new_node        # link the current node to new node
                    break
                current_Node = current_Node.next        #Transfer to the next node
                    
    def insertAfter(self,value, newVal):
        """
        Add a new node with the given newValue immediately After the first value node
        """        
        new_node = Node(newVal)             #create New Node
        if not self.includes(value):                   # if LinkedList Empty
            return "Value Not Found"
        else :                                  
            current_Node = self.head        #set the node_pointer which is looping over the LinkeList
            while current_Node.next != None:    
                if current_Node.value == value:    #check the value of current node before moving
                    new_node.next = current_Node.next   # link the new_node first
                    current_Node.next = new_node        # link the current node to new node
                    break
                current_Node = current_Node.next        #Transfer to the next node
                
    def insert(self,value):
        """
        The Insert method Take value as an argument then create a node to insert this node at the beginning of this list
        """

        # Creating Node and setting the value
        new_node=Node(value)

        #edge Case to add the node as  a head if the LinkedList Is Empty
        if not self.head:
            self.head=new_node
        else:
           new_node.next=self.head              #set the pointer to the new node to the head
           self.head=new_node                   # set the new node as the head of linkedList

    def includes(self, value):
        """
        This Function check if the list contain a node with specific value and retrun True if founded 
        """
        # To check if the LinkedList Empty Or Not
        if not self.head:
            return False
        else:
            current_Node = self.head        #set the node_pointer which is looping over the LinkeList
            # Step2: keep moving current_Node until you reach the last node
            while current_Node != None:
                if current_Node.value == value:
                    return True
                else:
                    current_Node = current_Node.next
            return False

    def linkedList_Lenght(self):
        """
        This Function will getting the the lenght of the array (size)
        """
        lenght=0                         #setting the length variable
        if not self.head:                   # if empty return zero
            return 0
        else : 
            current_Node = self.head            # looping until the end 
            while current_Node != None:             
                lenght+=1
                current_Node = current_Node.next
            return lenght

    def ll_kth_from_end(self,k):
        """
        This method  takes a number, k, as a parameter.
        Return the node’s value that is k from the end of the linked lis
        """

        length = self.linkedList_Lenght()               # get the length of linkedList         
        if length ==0:                                  # Empty LinkedList
            return "Empty LinkedList"                   
        if k >= length:                                 # k out of index case
            return "Greater Than List"                  # nigative values
        if k<0:
            return "Enter Positive Number"
        current_k = (length-k)-1                        # get the index of k in normal flow and -1 for indexing
        current_node = self.head
        for node in range(current_k):                   #looping and stop at the k Node 
            current_node=current_node.next
        return current_node.value


    def __str__(self):
        """
        This Method for Print the LinkedList in specific Formatting Style
        """
        current_Node = self.head
        linkedList_Serise = ''
        while current_Node != None:
            linkedList_Serise += f'{current_Node} -> '
            current_Node=current_Node.next
        linkedList_Serise+= 'NULL'
        return linkedList_Serise

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert(35)
    ll.insert(4)
    ll.append(5555)
    # print(ll.insertBefore(35,0))
    # print(ll.insertAfter(35,1))
    print(ll.ll_kth_from_end(1))
    print(ll)