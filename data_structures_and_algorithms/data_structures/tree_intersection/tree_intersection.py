from data_structures_and_algorithms.data_structures.Tree.tree import BinaryTree,Node

def tree_intersection(tree1,tree2):
    output=[]
    if tree1.root and tree2.root:
        first_list=tree1.preOrder()
        second_list=tree2.preOrder()       
        second_list=set(second_list)
        for i in first_list:
            if i in second_list:
                output.append(i)
    return output



if __name__ == "__main__":
    bt = BinaryTree()
    bt2 = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    
    bt2.root = Node(6)
    bt2.root.right = Node(5)
    bt2.root.left = Node(1)
    bt2.root.right.left = Node(6)
    bt2.root.left.left = Node(10)
    bt2.root.right.right = Node(2)
    
    print (tree_intersection(bt, bt2))