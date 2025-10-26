from data_structures.linkedlist import LinkedList

class Stack : 
    def __init__(self):
        self.list = LinkedList()
        
    def push(self,data):
        """
        Add a new element to the top of the stack.

        Args:
            value: The data to be pushed onto the stack.

        Behavior:
            Inserts the value at the top of the stack (head of the linked list).
            Updates the stack size accordingly.
        """

        self.list.prepend(data)     
            
    def pop(self):
        """
        Remove and return the top element of the stack.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty (underflow).

        Behavior:
            Removes the top element (head node) from the stack.
            Decrements the stack size.
        """

        if self.list.head is None:
            raise IndexError("Stack Underflow")
        value = self.list.head.data
        self.list.head = self.list.head.next
        self.list._size -= 1
        return value
        
    def peek(self, n=1):
        """
        Return the top 'n' elements of the stack without removing them.

        Args:
            n (int, optional): Number of top elements to retrieve. Default is 1.

        Returns:
            list: A list of the top 'n' elements, from top to bottom.

        Behavior:
            Traverses the stack from top and collects up to 'n' elements.
            Does not modify the stack.
        """

        count = min(n,len(self.list))
        def _gen():
            for i in range(count):
                yield self.list[i]
                    
        return list(_gen())
        
    def is_empty(self):
        """
        Check whether the stack is empty.

        Returns:
            bool: True if the stack has no elements, False otherwise.
        """

        if self.list._size == 0 : 
            return True
        else : 
            return False
    
    def search(self,value):
        """
        Search for a specific value in the stack.

        Args:
            value: The element to search for in the stack.

        Returns:
            int: The position of the element from the top of the stack (0-based index).
                Returns -1 if the element is not found.

        Behavior:
            Traverses the stack from the top to the bottom.
            Stops as soon as the element is found.
            Does not modify the stack.
        """

        for i in range(len(self.list)) : 
            if self.list[i] == value : 
                return i

        return -1
        
    def __len__(self):
        return self.list._size
    
    def __str__(self):
        items = []
        current = self.list.head
        while current:
            items.append(str(current.data))
            current = current.next
        return "Stack(top -> bottom): " + " -> ".join(items)
