class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Dog:
    def __init__(self,dog_name):
        self.name=dog_name    
        self.type='Dog'

class Cat:
    def __init__(self,cat_name):
        self.name=cat_name   
        self.type='Cat'

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, animal):
        node = Node(animal)
        # print(node.value.__class__.__name__)
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self,type):

        if self.is_empty():
            return 'Queue is empty'
        else:
            temp = self.front
            
            if temp.value.__class__.__name__ ==type:
                
                self.front = self.front.next
                temp.next = None
                return temp.value.name

            while(temp):
                if temp.next.value.__class__.__name__ ==type:
                    temp.next = temp.next.next
                    return temp.value.name
                temp = temp.next
            return temp.value.name


    def print_(self):
        temp = self.front
        str =""
        while (temp):
            str+=f'{temp.value.name} -> '
            temp = temp.next
        return str

    def is_empty(self):
        if not self.rear :
            return True
        else:
            return False


if __name__ == "__main__":
    sherry=Cat('sherry')
    ossccaar=Dog('ossccaar')
    owow=Dog('owow')

    animals=AnimalShelter()

    animals.enqueue(sherry)
    animals.enqueue(ossccaar)
    animals.enqueue(owow)
    print(animals.print_())
    print(animals.dequeue('Cat'))

    print(animals.print_())