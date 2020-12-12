
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):

        if self.is_empty():
            return 'Queue is empty'
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'

    def is_empty(self):
        if not self.rear :
            return True
        else:
            return False

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):

        if not self.top :
            return "Stack Is Empty"
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value


    def peek(self):

        if not self.is_empty():
            return self.top.value
        else :
            return "Stack Is Empty"

    def is_empty(self):
        if not self.top:
            return True
        else:
            return False


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push('cat')
    stack.peek()
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())

    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.is_empty())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
