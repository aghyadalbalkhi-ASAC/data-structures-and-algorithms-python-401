from data_structures_and_algorithms.data_structures.Tree.tree import BinaryTree,Node,BinarySearchTree
import pytest


# add the value the empty tree
def test_add_to_empty_tree(pr_BT): 
    pr_BT.add(4)
    assert pr_BT.root.value == 4
    
def test_preOrder(pr_BT):
    assert pr_BT.preOrder() == [4, -1, 3, 9, 6, 5, 8]

def test_inOrder(pr_BT):
    assert pr_BT.inOrder() == [-1, 3, 4, 5, 6, 8, 9]
    
def test_postOrder(pr_BT):
    assert pr_BT.postOrder() == [3, -1, 5, 8, 6, 9, 4]



# check the value the empty tree 
def test_empty_tree():
    pr_BT = BinarySearchTree()
    assert pr_BT.contains(55) == False
    

# check a values in ! empty tree
def test_contains_tree(pr_BT):
    assert pr_BT.contains(5) == True
    
# check a values in ! empty tree
def test_Not_contains_tree(pr_BT):
    assert pr_BT.contains(555) == False
    
    


@pytest.fixture
def pr_BT():
    binary_Tree = BinarySearchTree()
    binary_Tree.add(4)
    binary_Tree.add(9)
    binary_Tree.add(-1)
    binary_Tree.add(6)
    binary_Tree.add(3)
    binary_Tree.add(8)
    binary_Tree.add(5)
    return binary_Tree