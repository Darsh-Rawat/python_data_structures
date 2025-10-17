from data_structures.linkedlist import LinkedList
from data_structures.doubly_linkedlist import DoublyLinkedList
from data_structures.stack import Stack

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
l1.append(1)
l1.append(3)
# size = len(l1)

# for i in range(size//2) : # 0 - 1 : size - 1 = 3 = x
#     print(f"{i} : {size-1-i} : Sum : {l1[i] + l1[size-1-i]}")

s1 = Stack()
s1.push(10)
s1.push(11)
s1.push(12)
# print(s1.is_empty())
# print(len(s1))
print(s1.peek(n=2))
print(s1.search(12))    
