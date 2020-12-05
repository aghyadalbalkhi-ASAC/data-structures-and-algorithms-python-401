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

    def __str__(self):
        """
        This Method for Print the LinkedList in specific Formatting Style
        """
        current_Node = self.head
        print(current_Node)
        linkedList_Serise = ''
        while current_Node != None:
            linkedList_Serise += f'{current_Node} -> '
            current_Node=current_Node.next
        linkedList_Serise+= 'NULL'
        return linkedList_Serise

    