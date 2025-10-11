from core.node import DoubleNode

class DoublyLinkedList : 
    # Phase-1
    
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self,data):
        if self.head is None:
            self.head = DoubleNode(data)
            self._size += 1
        else:
            temp = self.head
            while temp.next != None :
                temp = temp.next
            newNode = DoubleNode(data)
            newNode.prev = temp
            temp.next = newNode
            self._size += 1
            
    
    def display(self):
        """
        Return a list of all node values in the linked list in order.

        Traverses the linked list from head to end and collects
        each node's data into a Python list.

        Returns:
            list: A list of all node data in the linked list.

        Example:
            ll = DoublyLinkedList()
            ll.append(10)
            ll.append(20)
            ll.append(30)
            ll.display()  # returns [10, 20, 30]
        
        """
        temp = self.head
        if not temp : 
            return []
        else : 
            content = []
            while(temp != None) : 
                content.append(temp.data)
                temp = temp.next
            return content
    
    def size(self):
        """
        Return the number of nodes currently in the linked list.

        Returns:
            int: The number of nodes in the list.

        Example:
            ll.size()  # 3 if there are 3 nodes
        """
        return self._size