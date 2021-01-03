from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Queue

class Node :
    """
    a class Node which present the nodes in the tree where every node contains the left address for left child
    and the stored data and the right address for right child
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    BinaryTree is a one of the data strcuture that represent hierarchical data .
    """

    def __init__(self):
        self.root = None
        self.max = 0


    def preOrder(self):
        
        #1. Initialize  //  To store the values of roots in Tress (Parents)
        output = [] 
        
        #2. Define the closure
        def _walk(node):
            output.append(node.value)
            
            # if left node has a child  (reach the leaf nodes)
            if node.left:
                _walk(node.left)
            
            # if right node has a child  (reach the leaf nodes)
            if node.right:
                _walk(node.right)
                
        #3. Call the closure with initial value
        _walk(self.root)

        #4. Return the resul

        return output

    def inOrder(self):
        #1. Initialize  //  To store the values of roots in Tress (Parents)
        output = [] 
        
        #2. Define the closure
        def _walk(node):
            
            # if left node has a child  (reach the leaf nodes)
            if node.left:
                _walk(node.left)
            
            output.append(node.value)
            
            # if right node has a child  (reach the leaf nodes)
            if node.right:
                _walk(node.right)
                
        #3. Call the closure with initial value
        _walk(self.root)

        #4. Return the resul

        return output


    def postOrder(self):
        #1. Initialize  //  To store the values of roots in Tress (Parents)
        output = [] 
        
        #2. Define the closure
        def _walk(node):
            
            # if left node has a child  (reach the leaf nodes)
            if node.left:
                _walk(node.left)            
            # if right node has a child  (reach the leaf nodes)
            if node.right:
                _walk(node.right)

            output.append(node.value)
        #3. Call the closure with initial value
        _walk(self.root)

        #4. Return the resul

        return output
    
    def find_maximum_value(self):
        
        # if Binary_Tree Empty
        if not self.root:
            raise AssertionError ('Binary Tree is Empty')
        
        #2. Define the closure
        def _walk(node):
            if node.value > self.max:
                self.max = node.value
            # if left node has a child  (reach the leaf nodes)
            if node.left:
                _walk(node.left)
            
            # if right node has a child  (reach the leaf nodes)
            if node.right:
                _walk(node.right)
                
        #3. Call the closure with initial value
        _walk(self.root)

        #4. Return the max

        return self.max
    
    def breadth_first(self,node):
    # INPUT  <-- root node
    # OUTPUT <-- front node of queue to console

    #Queue breadth <-- new Queue()
        results =[]
        breadth = Queue()
        breadth.enqueue(node)
        
        try:
            while breadth.peek():
                front = breadth.dequeue()
                results.append(front.value)

                if front.left:
                    breadth.enqueue(front.left)

                if front.right:
                    breadth.enqueue(front.right)
        except AttributeError :
            pass
        return results
class BinarySearchTree(BinaryTree):
    
    def add(self,value):
        
        # if there is not root 
        if not self.root:
            self.root = Node(value)
            
        # if there is a root 
        else:
            def _walk(node):
                # if the value less than the root Go left
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)        
                        return
                    else:
                        _walk(node.left)    
                        
                # if the value greater than the root Go right
                else:
                    if not node.right:
                        node.right = Node(value)        
                        return
                    else:
                        _walk(node.right)
            _walk(self.root)
                        
    def contains(self,value):
        
        # if there is not root // empty tree
        if not self.root:
            return False
            
        # if there is a root 
        else:
            def _walk(node):
                # check the root value 
                if value == node.value:
                    return True
                # if the value less than the root Go left
                if value < node.value:
                    if node.left:
                        return _walk(node.left)
                    else:
                        return False
                # if the value greater than the root Go right
                else:
                    if node.right:       
                        return _walk(node.right)
                    else:
                        return False           
            return _walk(self.root)
    

if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    bt.breadth_first(bt.root)
    # print(bt.preOrder())
    # print(bt.inOrder())
    # print(bt.postOrder())
    print(bt.find_maximum_value())
    # bst = BinarySearchTree()
    # bst.add(4)
    # bst.add(9)
    # bst.add(-1)
    # bst.add(6)
    # bst.add(3)
    # bst.add(8)
    # bst.add(5)

    # assert bst.root.value == 4
    # assert bst.root.left.value == -1
    # assert bst.root.right.value == 9
    # assert bst.root.left.right.value == 3
    # assert bst.root.right.left.left.value == 5
    # print('=====All passed======')
    
    # print(bst.contains(8))