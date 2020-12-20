
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
        temp = self.front
        if self.is_empty():
            raise AttributeError ('Queue is empty')
        else:
            
            self.front = self.front.next
            temp.next = None
        if self.front == None:
            self.rear = None
        return temp.value

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            raise AttributeError ('Queue is empty')

    def is_empty(self):
        if self.rear == None and self.front == None :
            return True
        else:
            return False

    def print_(self):
        temp = self.front
        str = ''
        while temp:
            str += f'{temp.value} - > '
            temp = temp.next
        return str

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
            raise AttributeError ('Queue is empty')
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value


    def peek(self):

        if not self.is_empty():
            return self.top.value
        else :
            raise AttributeError ('Queue is empty')

    def is_empty(self):
        if not self.top:
            return True
        else:
            return False


if __name__ == "__main__":
    stack = Stack()
    # print('check when initlize the stack ',stack.is_empty())
    # stack.push(5)
    # stack.push(6)
    # stack.push('cat')
    # print(stack.peek())
    # print('check after adding some items ',stack.is_empty())

    # stack.pop()
    # stack.pop()
    # print(stack.peek())
    # print('check after pop() some items ',stack.is_empty())

    # stack.pop()
    # print(stack.peek())
    # print('check after pop() all items ',stack.is_empty())
    # print(stack.is_empty())

    # stack.push(5)
    # stack.push(6)
    # stack.push('cat')
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # print(stack.is_empty())

    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    # queue.enqueue(5)
    # queue.enqueue(77)
    # queue.dequeue()
    # print(queue.print_())
