class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise AttributeError("Stack is empty")
        popped = self.top.value
        self.top = self.top.next
        return(popped)

    def peek(self):
        if self.top == None:
            raise AttributeError("Stack is empty.")
        return self.top.value

    def isEmpty(self):
        if self.top:
            return False
        return True

class PseudoQueue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.peek() == None and self.stack2.peek() == None :
            return "Queue is Empty"
        if self.stack2.top ==None :
            while (self.stack1.top):
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


if __name__ == "__main__":
    aghyad = PseudoQueue()
    aghyad.enqueue(5)
    aghyad.enqueue(6)
    aghyad.enqueue(77)
    aghyad.dequeue()
    aghyad.dequeue()

print(aghyad.stack2.peek())
