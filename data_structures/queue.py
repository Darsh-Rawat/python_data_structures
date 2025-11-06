from data_structures.linkedlist import LinkedList

class Queue : 
    def __init__(self) :        
        """
        Initializes a new empty Queue object.

        Creates a new LinkedList object to store the queue data.
        """
        self.list = LinkedList()
        self.front = None
        self.rear = None
    
    def enqueue(self,value) : 
        """
        Adds a new element to the end of the queue.

        Args:
            value: The value to be added to the queue.

        Behavior:
            - If the queue is empty, sets the front and rear to the new node.
            - If the queue is not empty, sets the rear to the new node.

        Example:
            q.enqueue(10)
            # Adds 10 to the end of the queue
        """
        
        new_node = self.list.append(value)
        
        if self.front is None : 
            self.front = new_node
            self.rear = new_node
        else :
            self.rear = new_node 
    
    def dequeue(self) : 
        """
        Removes and returns the element at the front of the queue.
        
        Returns:
            any: The value of the removed element.
            
        Raises:
            ValueError: If the queue is empty.

        Behavior:
            - If the queue is empty, raises a ValueError.
            - If the queue is not empty, removes the front element and returns its value.

        Example:
            q.dequeue()
            # Removes and returns the front element of the queue
        """
        if self.front is None : 
            raise ValueError("Queue is empty.")
        
        value = self.front.data
        self.front = self.front.next
        
        if self.front is None : 
            self.rear = None
        
        # Decrease the list size
        self.list._size -= 1
        
        return value

    def peek(self) : 
        return self.front.data

    def __len__(self):
        return len(self.list)