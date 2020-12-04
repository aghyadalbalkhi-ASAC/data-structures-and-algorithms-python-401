class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else:
           new_node.next=self.head
           self.head=new_node    

    def append(self, data):
        # Step0: create the data node
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            # Step1: initialize current with head (index zero)
            current = self.head
            # Step2: keep moving current until you reach the last node
            while current.next != None:
                current = current.next
            # current is the last node
            # Step3: make the current points to the new node
            current.next = node
        self.size += 1

    def __len__(self):
        return self.size

    def __str__(self):
        pass


if __name__ == "__main__":
    node1 = Node(5)
    print(node1.value)
    node2 = Node(7)
    node1.next = node2
    
    print(node1.value)
    # node1 -> node2 -> None







# """
# Class Node will Create a Node which present one item in the list
# """

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     """
# The LinkedList Class will content the list of nodes that we created using the Node class and link thoses togather 
#     """
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     # put your LinkedList implementation here
#     pass
