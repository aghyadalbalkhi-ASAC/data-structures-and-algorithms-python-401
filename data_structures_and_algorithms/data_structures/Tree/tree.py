
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
    print(bt.preOrder())
    print(bt.inOrder())
    print(bt.postOrder())
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