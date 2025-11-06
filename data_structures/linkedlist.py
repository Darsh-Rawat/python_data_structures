from core.node import Node

class LinkedList : 
    # Phase-1
    
    def __init__(self):
        self.head = None
        self._size = 0
        
    def append(self,data) : 
        """
        Add a new node with the given data at the end of the linked list.

        Args:
            data (any): The value to store in the node.

        Returns:
            Node: The appended node.

        Example:
            ll = LinkedList()
            ll.append(10)
        """
        if self.head is None:  
            self.head = Node(data)
            self._size += 1
            return self.head
            
        else : 
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next = Node(data)   
            self._size += 1
        
            return temp.next
            
                     
    def prepend(self,data) : 
        """
        Add a new node with the given data at the beginning of the linked list.

        Args:
            data (any): The value to store in the new node.

        Returns:
            None

        Behavior:
            - Creates a new node and makes it the head.
            - The previous head becomes the second node.
            - Updates the list size.

        Example:
            ll = LinkedList()
            ll.prepend(5)
            # List now: 5 -> existing nodes
        """
        if self.head is None:  
            self.head = Node(data)
            self._size += 1
        else : 
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            self._size += 1
            
    def insert_at(self,index,data) : 
        """
        Insert a new node with the given data at the specified position.

        Args:
            index (int): Position at which to insert the new node (0-based).
            data (any): Value to store in the new node.

        Returns:
            None

        Raises:
            IndexError: If index is out of bounds (less than 0 or greater than size).

        Behavior:
            - If index is 0, prepends the node.
            - If index equals current size, appends the node.
            - Otherwise, traverses to the position and inserts the node.

        Example:
            ll.insert_at(1, 15)
            # Inserts 15 at position 1
        """
        if index == 0 : 
            self.prepend(data)   
        elif index == self._size : 
            self.append(data)
        else : 
            prev = self.head
            for i in range(index-1):
                prev = prev.next
                
            newNode = Node(data)
            current = prev.next
            prev.next = newNode
            newNode.next = current
            self._size += 1
        
            
    def delete(self,data):
        """
        Remove the first node in the list that contains the specified data.

        Args:
            data (any): The value to delete from the list.

        Returns:
            bool: True if a node was deleted, False if the value was not found.

        Behavior:
            - Traverses the list to find the node with matching data.
            - Updates links to remove the node from the chain.
            - Decrements the list size if deletion occurs.

        Example:
            ll.delete(20)
            # Removes first node with value 20
        """
        if self.head is None : 
            return None
        else : 
            prev = self.head
            current = self.head.next
            while(current is not None) : 
                if current.data == data : 
                    prev.next = current.next
                    self._size -= 1
                    return True
                prev = current
                current = current.next
            else:
                return False
                     
        
    def search(self,data):
        """
        Check if the linked list contains a node with the given data.

        Args:
            data (any): The value to search for.

        Returns:
            bool: True if the value exists in the list, False otherwise.

        Behavior:
            - Traverses the list from head to tail.
            - Stops traversal once the value is found.

        Example:
            ll.search(10)  # True if 10 exists, False otherwise
        """
        if self.head is None : 
            return None
        else : 
            temp = self.head
            while(temp is not None) : 
                if temp.data == data : 
                    return True
                temp = temp.next
            else:
                return False
            
    def __get_at(self,index) :
        """
        Retrieve the data stored at a specific index in the linked list.

        Args:
            index (int): The position of the node whose data should be returned (0-based index).

        Returns:
            Any: The data stored in the node at the given index.

        Raises:
            IndexError: If the index is out of range or the list is empty.
        """
        if self.head is None:
            raise IndexError("Cannot access element from an empty linked list.")
        elif index < 0 or index >= self._size : 
            raise IndexError("Index out of range.")
        else : 
            temp = self.head
            for i in range(index) :
                temp = temp.next
            return temp.data
 
        
    def display(self):
        """
        Return a list of all node values in the linked list in order.

        Traverses the linked list from head to end and collects
        each node's data into a Python list.

        Returns:
            list: A list of all node data in the linked list.

        Example:
            ll = LinkedList()
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
    
    def reverse(self) :
        """
        Reverses the linked list in place.

        This method modifies the current linked list by reversing the order 
        of its nodes. After calling this method, the head of the list will 
        point to the previous tail, and all node connections will be reversed.

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.append(3)
            >>> ll.reverse()
            >>> ll.display()
            3 -> 2 -> 1
        """
        curr = self.head
        prev = None
        while curr : 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __getitem__(self, index):
        return self.__get_at(index)
