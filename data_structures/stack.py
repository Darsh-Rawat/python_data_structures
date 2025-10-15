from data_structures.linkedlist import LinkedList

class Stack : 
    def __init__(self):
        self.list = LinkedList()
        
    def push(self,data):
        self.list.prepend(data)     
            
    def pop(self):
        if self.list.head is None:
            raise IndexError("Stack Underflow")
        value = self.list.head.data
        self.list.head = self.list.head.next
        self.list._size -= 1
        return value
        
    def peek(self):
        return self.list.head.data
        
    def is_empty(self):
        if self.list._size == 0 : 
            return True
        else : 
            return False
        
    def __len__(self):
        return self.list._size