from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack,Queue


def test_Stack_is_empty():
    stack = Stack()
    actual= stack.is_empty()
    expexted=True
    assert actual==expexted

def test_Queue_is_empty():
    queue = Queue()
    actual= queue.is_empty()
    expexted=True
    assert actual==expexted

def test_Stack_push():
    stack = Stack()
    stack.push(5)
    stack.push(6)
    actual=stack.peek()
    expexted=6
    assert actual==expexted

def test_Queue_enqueue():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    actual=queue.peek()
    expexted=4
    assert actual==expexted



def test_Stack_pop():
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.pop()
    actual=stack.peek()
    expexted=5
    assert actual==expexted

def test_Queue_dequeue():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    actual=queue.peek()
    expexted=5
    assert actual==expexted