
from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList,Node

class Hashmap:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        idx = self.get_hash(key)
        if not self.map[idx]:
            self.map[idx] = LinkedList()
        self.map[idx].insert([key, value])

    def get(self, key):
        idx = self.get_hash(key)
        if self.map[idx]:
            current = self.map[idx].head
            while current:
                if current.value[0] == key :
                    return current.value[1]
                current = current.next
        else:
            return None
    def contains(self,key):
        if  self.map[self.get_hash(key)]:
            return True
        else:
            return False


    def get_hash(self, key):
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch)
        hashed = ascii_total * 17
        hashed = hashed % self.size
        return hashed




def left_join(hash1,hash2):
    output = []

    for element in hash1.map:

        if element != None:

            for e in element:
                element_list = []
                element_list.append(e[0])
                element_list.append(e[1])
        
                if hash2.contains(e[0]):
                    element_list.append(hash2.get(e[0]))
                else:
                    element_list.append(None)
        
                output.append(element_list)
       
    return output