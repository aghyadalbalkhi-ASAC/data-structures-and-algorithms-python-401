from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList


def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


#Add_First To Empty LinkedList
def test_LinkedList_insert():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    assert test_LinkedList.head.value == 0

def test_LinkedList_insertBefore():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(5)
    test_LinkedList.insert(35)
    test_LinkedList.insert(4)
    test_LinkedList.append(5555)
    test_LinkedList.insertBefore(35,0)
    assert test_LinkedList.__str__() == "{ 4 } -> { 0 } -> { 35 } -> { 5 } -> { 5555 } -> NULL"

def test_LinkedList_insertAfter():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(5)
    test_LinkedList.insert(35)
    test_LinkedList.insert(4)
    test_LinkedList.append(5555)
    test_LinkedList.insertAfter(35,1)
    assert test_LinkedList.__str__() == "{ 4 } -> { 35 } -> { 1 } -> { 5 } -> { 5555 } -> NULL"


#Add_ To Not Empty LinkedList From the beginning 
def test_LinkedList_insert_second_Test():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    assert test_LinkedList.head.value == 0
    test_LinkedList.insert(1)
    assert test_LinkedList.head.next.value == 0

#To Check if the LinkedList contain a node with specific value 
def test_LinkedList_includes():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.includes(1) == True
    assert test_LinkedList.includes(100) == False


def test_LinkedList_kthFromEnd():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(5)
    test_LinkedList.insert(35)
    test_LinkedList.insert(4)
    test_LinkedList.append(5555)
    test_LinkedList.insertAfter(35,1)
    assert test_LinkedList.ll_kth_from_end(0) == 5555
    assert test_LinkedList.ll_kth_from_end(1) == 5

#To Check if the LinkedList contain a node with specific value 
def test__str__():
    test_LinkedList = LinkedList()
    test_LinkedList.insert('9')
    test_LinkedList.insert('1')
    test_LinkedList.insert('-')
    test_LinkedList.insert('D')
    test_LinkedList.insert('I')
    test_LinkedList.insert('V')
    test_LinkedList.insert('O')
    test_LinkedList.insert('C')
    test_LinkedList.insert('_')
    test_LinkedList.insert('0')
    test_LinkedList.insert('2')
    test_LinkedList.insert('0')
    test_LinkedList.insert('2')
    assert test_LinkedList.__str__() == "{ 2 } -> { 0 } -> { 2 } -> { 0 } -> { _ } -> { C } -> { O } -> { V } -> { I } -> { D } -> { - } -> { 1 } -> { 9 } -> NULL"