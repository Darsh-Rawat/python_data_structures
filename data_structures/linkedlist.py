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
            None

        Example:
            ll = LinkedList()
            ll.append(10)
        """
        if self.head == None:  
            self.head = Node(data)
            self._size += 1
            
        else : 
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next = Node(data)   
            self._size += 1
            
                     
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
        if self.head == None:  
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
        ...
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
        ...
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
        ...
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
                
    def size(self) : 
        """
        Return the number of nodes currently in the linked list.

        Returns:
            int: The number of nodes in the list.

        Example:
            ll.size()  # 3 if there are 3 nodes
        """
        return self._size