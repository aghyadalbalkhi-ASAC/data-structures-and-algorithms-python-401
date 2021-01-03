from data_structures_and_algorithms.data_structures.Tree.tree import BinaryTree,Node

# This function to check the Fizz and Buzz status and return a results 

def fizz_buzz(value):
    if value % 5 == 0 and value % 3 ==0:
        return "Fizz_Buzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)
    
    
def FizzBuzzTree(tree):
    
    fizz_buzz_Tree = BinaryTree()
    
    if not tree.root:
        raise Exception ('Tree is Empty')
    
    def _walk(node):
        new_node= Node(fizz_buzz(node.value))
        if node.left:
            new_node.left = _walk(node.left)
        if node.right:
            new_node.right = _walk(node.right)
        return new_node
    
    fizz_buzz_Tree.root=_walk(tree.root)
    return fizz_buzz_Tree

    
if __name__ == "__main__":
    
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(9)
    tree.root.right.right = Node(15)
    
    print(tree.root.value)
    print(tree.root.left.value)
    print(tree.root.right.value)
    print(tree.root.right.right.value)

    test_tree=FizzBuzzTree(tree)
    print(test_tree.root.value)
    print(test_tree.root.left.value)
    print(test_tree.root.right.value)
    print(test_tree.root.right.right.value)