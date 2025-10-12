from data_structures.linkedlist import LinkedList
from data_structures.doubly_linkedlist import DoublyLinkedList

# l1 = LinkedList()
# l1.append(2)
# print(l1.display(), l1.size())
# l1.prepend(1)
# print(l1.display(), l1.size())
# l1.append(3)
# print(l1.display(), l1.size())
# l1.insert_at(1,1.5)
# print(l1.display(), l1.size())
# l1.delete(1.5)
# print(l1.display(), l1.size())
# print(l1.search(67))

# l2 = DoublyLinkedList()
# l2.append(2)
# l2.append(3)
# print(l2.display())
# print(l2.size())

l1 = LinkedList()
l1.append(4)
l1.append(2)
l1.append(2)
l1.append(3)
size = len(l1)

for i in range(size//2) : 
    print(f"{i} : {size-1-i} : Sum : {l1[i] + l1[size-1-i]}")
    
for i in l1 : 
    print(i)

    
