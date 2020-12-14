#  //////////////////////// Node Class //////////////////////////

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


#  //////////////////////// Stack Class //////////////////////////
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):

        # Create New Node 
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise AttributeError("Stack is empty")
        temp = self.top.value
        self.top = self.top.next
        return(temp)

    def peek(self):
        if self.top == None:
            raise AttributeError("Stack is empty.")
        return self.top.value

    def isEmpty(self):
        return self.top == None

#  //////////////////////// PseudoQueue Class //////////////////////////
class PseudoQueue:
    def __init__(self):
        self.stack_En=Stack()
        self.stack_De=Stack()

    def enqueue(self,value):
        self.stack_En.push(value)

    def dequeue(self):
        pop_item = None
        if self.stack_En.peek() == None :
            return "Queue is Empty"

            
        while (self.stack_En.top):
            self.stack_De.push(self.stack_En.pop())
        pop_item = self.stack_De.pop()

        while (self.stack_De.top):
                self.stack_En.push(self.stack_De.pop())

        return pop_item

    def print_(self):
        temp = self.stack_En.top
        while (temp):
            print(temp.value)
            temp = temp.next
            




if __name__ == "__main__":
    aghyad = PseudoQueue()
    aghyad.enqueue(5)
    aghyad.enqueue(6)
    aghyad.enqueue(77)
    aghyad.dequeue()
    aghyad.print_()
